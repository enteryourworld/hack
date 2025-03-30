from django.shortcuts import render
import requests
import json
from django.conf import settings
from urllib.parse import quote
import certifi
import os
from urllib3.exceptions import InsecureRequestWarning

# Настройка SSL
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def ask_gigachat(activity):
    """Запрос к GigaChat API для поиска компаний по тематике"""
    if not activity or activity == 'не указана':
        return None
    
    try:
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        
        prompt = (
            f"Найди 5 известных компаний или сообществ ВКонтакте в тематике '{activity}'. "
            "Предоставь ответ в формате: "
            "1. Название компании (ссылка vk.com/example) - краткое описание\n"
            "2. Название компании (ссылка vk.com/example) - краткое описание\n"
            "..."
        )
        
        payload = json.dumps({
            "model": "GigaChat",
            "messages": [{
                "role": "user", 
                "content": prompt
            }],
            "temperature": 0.7,
            "max_tokens": 500
        })
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {settings.GIGACHAT_TOKEN}'
        }

        response = requests.post(
            url, 
            headers=headers, 
            data=payload, 
            verify=False,
            timeout=15
        )
        response.raise_for_status()
        
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    
    except Exception as e:
        print(f"GigaChat Error: {str(e)}")
        return None

def group_info(request):
    context = {}
    
    if request.method == 'POST':
        group_name = request.POST.get('group_name', '').strip()
        if group_name:
            try:
                # Основной запрос информации о группе
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
                    context['error'] = f"Ошибка VK API: {data['error']['error_msg']}"
                elif not data.get('response', {}).get('groups'):
                    context['error'] = f"Группа '{group_name}' не найдена"
                else:
                    group = data['response']['groups'][0]
                    context['group'] = {
                        'name': group.get('name'),
                        'screen_name': group.get('screen_name'),
                        'members': f"{group.get('members_count', 0):,}".replace(',', ' '),
                        'activity': group.get('activity', 'не указана'),
                        'description': group.get('description', 'нет описания'),
                        'photo': group.get('photo_200'),
                        'url': f"https://vk.com/{group.get('screen_name')}",
                        'status': group.get('status', '')
                    }
                    context['searched_name'] = group_name
                    
                    # Запрашиваем похожие компании у GigaChat
                    if context['group']['activity'] != 'не указана':
                        context['gigachat_recommendations'] = ask_gigachat(context['group']['activity'])
            
            except Exception as e:
                context['error'] = f"Произошла ошибка: {str(e)}"
        else:
            context['error'] = 'Введите название группы'
    
    return render(request, 'group_info.html', context)
