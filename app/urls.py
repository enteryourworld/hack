from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_info, name='vk_group_search'),
]
