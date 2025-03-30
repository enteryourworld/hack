from django.shortcuts import render, redirect
import requests
import json
from django.conf import settings
from urllib.parse import quote
import certifi
import os
from urllib3.exceptions import InsecureRequestWarning
import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from .models import VKTheme
from datetime import datetime, timedelta

# Настройка SSL
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def collect_vk_themes(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name', '').strip()
        if group_name:
            try:
                response = requests.get(
                    'https://api.vk.com/method/groups.getById',
                    params={
                        'group_id': quote(group_name),
                        'fields': 'activity',
                        'access_token': settings.VK_SERVICE_TOKEN,
                        'v': '5.199'
                    },
                    timeout=10
                )
                data = response.json()

                if 'response' in data and data['response']['groups']:
                    activity = data['response']['groups'][0].get('activity', 'не указана')
                    if activity != 'не указана':
                        theme, created = VKTheme.objects.get_or_create(name=activity)
                        theme.popularity += 1
                        theme.save()
                        return redirect('popular_themes')
            
            except Exception as e:
                print(f"Error: {str(e)}")
    
    return render(request, 'collect_theme.html')

def popular_themes(request):
    # Топ-10 популярных тематик за последний месяц
    time_threshold = datetime.now() - timedelta(days=30)
    themes = VKTheme.objects.filter(
        last_updated__gte=time_threshold
    ).order_by('-popularity')[:10]
    
    return render(request, 'popular_themes.html', {'themes': themes})

def get_vk_data(group_name):
    """Получение данных VK (оригинальная функция без изменений)"""
    try:
        response = requests.get(
            'https://api.vk.com/method/groups.getById',
            params={
                'group_id': quote(group_name),
                'fields': 'members_count,description,photo_200,activity,status',
                'access_token': settings.VK_SERVICE_TOKEN,
                'v': '5.199'
            },
            timeout=10
        )
        data = response.json()

        if 'error' in data:
            return {'error': data['error']['error_msg']}
        
        if not data.get('response', {}).get('groups'):
            return {'error': f"Группа '{group_name}' не найдена"}
        
        group = data['response']['groups'][0]
        return {
            'name': group.get('name'),
            'screen_name': group.get('screen_name'),
            'members': f"{group.get('members_count', 0):,}".replace(',', ' '),
            'activity': group.get('activity', 'не указана'),
            'description': group.get('description', 'нет описания'),
            'photo': group.get('photo_200'),
            'url': f"https://vk.com/{group.get('screen_name')}",
            'status': group.get('status', ''),
            'source': 'vk'
        }
    except Exception as e:
        return {'error': str(e)}

def get_telegram_data(channel_username):
    """Получение данных Telegram (адаптировано под group_info.html)"""
    async def async_get():
        async with TelegramClient('session_name', settings.TELEGRAM_API_ID, settings.TELEGRAM_API_HASH) as client:
            username = channel_username.lstrip('@')
            try:
                channel = await client.get_entity(username)
                full_info = await client(GetFullChannelRequest(channel=channel))
                
                # Получаем 3 последних поста для отображения
                messages = await client.get_messages(channel, limit=3)
                last_posts = [msg.text for msg in messages if msg.text]
                
                return {
                    'name': channel.title,
                    'screen_name': channel.username,
                    'description': getattr(full_info.full_chat, 'about', 'нет описания'),
                    'photo': getattr(channel, 'photo', None),  # Для совместимости с шаблоном
                    'url': f"https://t.me/{channel.username}",
                    'last_posts': last_posts,
                    'source': 'telegram',
                    'members': None,  # Нет данных о подписчиках
                    'activity': 'Telegram-канал',  # Заглушка для совместимости
                    'status': ''  # Пустой статус для совместимости
                }
            except Exception as e:
                print(f"Telegram Error: {str(e)}")
                return None

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(async_get())
    finally:
        loop.close()

def ask_gigachat(context, source):
    """Универсальный запрос к GigaChat"""
    try:
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        
        if source == 'vk':
            prompt = (
                f"Найди 5 известных компаний ВКонтакте в тематике '{context['group']['activity']}'. "
                "Формат: 1.Ссылка:(vk.com/ссылка)/подробное писание\n"
                "2. Ссылка:(vk.com/ссылка)/подробное писание\n..."
            )
        else:
            prompt = (
                f" Проанализируй и Строго перечисли 5 похожих Telegram-каналов для '{context['group']['name']}'. "
                "Основано на этих постах:\n" + "\n".join([f"- {post}" for post in context['group']['last_posts']][:3]) + "\n"
                "Только список в формате:\n"
                "1.Название канала\n  t.me/channel1\n описание"
                "2.Название канала\n t.me/channel2\n описание"
                "...\n"
                "Без вводных фраз, описаний и дополнительного текста !"
            )
        
        payload = json.dumps({
            "model": "GigaChat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1000
        })
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {settings.GIGACHAT_TOKEN}'
        }

        response = requests.post(url, headers=headers, data=payload, verify=False, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    
    except Exception as e:
        print(f"GigaChat Error: {str(e)}")
        return None
import logger
def group_info(request):
    """Основная view-функция для анализа групп VK и Telegram"""
    # Инициализируем контекст с None для всех возможных переменных
    context = {
        'error': None,
        'group': None,
        'searched_name': None,
        'gigachat_recommendations': None
    }

    if request.method == 'POST':
        try:
            # Получаем параметры из формы
            source = request.POST.get('source', 'vk')
            name = request.POST.get('group_name', '').strip()
            
            # Валидация ввода
            if not name:
                raise ValueError("Пожалуйста, введите название группы/канала")
            
            # Получаем данные в зависимости от источника
            if source == 'vk':
                data = get_vk_data(name)
                
                # Проверка ответа от VK API
                if not data or 'error' in data:
                    error_msg = data.get('error', 'Не удалось получить данные группы VK')
                    raise ValueError(error_msg)
                
                # Дополнительная проверка для VK
                if data['activity'] == 'не указана':
                    context['warning'] = "Тематика группы не указана"
                
            elif source == 'telegram':
                data = get_telegram_data(name)
                
                # Проверка ответа от Telegram
                if not data:
                    raise ValueError("Не удалось получить данные Telegram-канала")
                
                # Проверка наличия постов
                if not data.get('last_posts'):
                    context['warning'] = "В канале нет публичных сообщений"
            else:
                raise ValueError("Неподдерживаемый источник данных")

            # Заполняем контекст
            context['group'] = data
            context['searched_name'] = name
            context['source'] = source

            # Получаем рекомендации если есть данные для анализа
            if (source == 'vk' and data.get('activity') != 'не указана') or \
               (source == 'telegram' and data.get('last_posts')):
                
                try:
                    recommendations = ask_gigachat(context, source)
                    if recommendations:
                        context['gigachat_recommendations'] = recommendations
                    else:
                        context['warning'] = "Не удалось получить рекомендации"
                except Exception as e:
                    logger.error(f"GigaChat error: {str(e)}")
                    context['warning'] = "Ошибка при анализе данных"

        except requests.exceptions.RequestException as e:
            context['error'] = f"Ошибка соединения: {str(e)}"
            logger.error(f"Network error: {str(e)}")
        
        except ValueError as e:
            context['error'] = str(e)
        
        except Exception as e:
            context['error'] = "Произошла непредвиденная ошибка"
            logger.exception("Unexpected error in group_info:")
    
    return render(request, 'group_info.html', context)
