from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django_hosts.resolvers import reverse
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = 'app/home.html'


class LoginInterfaceView(LoginView):
    template_name = 'app/login.html'


class LogoutView(LogoutView):
    template_name = 'app/logout.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'app/signup.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home', permanent=True, *args, **kwargs)
        return super().get(request, *args, **kwargs)
