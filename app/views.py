from django.shortcuts import render
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

# Настройка SSL
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
                "Формат: 1. Название (vk.com/ссылка) - описание\n"
                "2. Название (vk.com/ссылка) - описание\n..."
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

def group_info(request):
    """Основная view (адаптирована под оригинальный group_info.html)"""
    context = {}
    
    if request.method == 'POST':
        source = request.POST.get('source', 'vk')
        name = request.POST.get('group_name', '').strip()
        
        if name:
            if source == 'vk':
                data = get_vk_data(name)
            else:
                data = get_telegram_data(name)
            
            if data and 'error' not in data:
                context['group'] = data
                context['searched_name'] = name
                
                # Запрашиваем рекомендации если есть тематика (VK) или посты (Telegram)
                if (source == 'vk' and data['activity'] != 'не указана') or (source == 'telegram' and data['last_posts']):
                    context['gigachat_recommendations'] = ask_gigachat(context, source)
            else:
                context['error'] = data.get('error', 'Не удалось получить данные')
        else:
            context['error'] = 'Введите название'
    
    return render(request, 'group_info.html', context)
