from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class HomeView(TemplateView):
    template_name = 'app/home.html'


class LoginInterfaceView(LoginView):
    template_name = 'app/login.html'


class LogoutView(LogoutView):
    template_name = 'app/logout.html'
