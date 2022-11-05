from django.urls import path
from app import views

app_name = 'app'

urltpatterns = [
    path('', views.home, name='home'),
]