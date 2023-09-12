from django.urls import path
from main.views import show_main,show_home

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('home/', show_home, name='show_home')
]