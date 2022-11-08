from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Url


def root(request, url_hash):
    url = get_object_or_404(Url, url_hash=url_hash)
    url.visited()

    return redirect(url.url_full)


class UrlsShortified(ListView):
    model = Url
    context_object_name = 'urls'
    template_name = 'urls/urls_list.html'