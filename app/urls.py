from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_vk_companies, name='chat-view'),
    # Добавьте другие маршруты по аналогии
]