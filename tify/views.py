from django.shortcuts import redirect
from django_hosts.resolvers import reverse

def redirect_home(request):
    render(request, redirect(reverse('home', host='app'), {})