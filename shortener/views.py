from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .forms import UrlsForm
from .models import Url


def root(request, url_hash):
    url = get_object_or_404(Url, url_hash=url_hash)
    url.visited()

    return redirect(url.url_full)


class UrlCreateView(CreateView):
    model = Url
    form_class = UrlsForm
    success_url = 'urls/list'
    template_name = 'urls/url_new.html'
    def get_login_url(self):
        login_url = reverse()
        return str(login_url)

class UrlListView(LoginRequiredMixin, ListView):
    model = Url
    context_object_name = 'urls'
    template_name = 'urls/urls_list.html'
    login_url = reverse_lazy('admin', urlconf='tify.urls_admin')

class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'
    template_name = 'urls/url_detail.html'
