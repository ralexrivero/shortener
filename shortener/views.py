from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.views.generic.edit import DeleteView
from django.http.response import HttpResponseRedirect

from .forms import UrlsForm
from .models import Url


def root(request, url_hash):
    url = get_object_or_404(Url, url_hash=url_hash)
    url.visited()

    return redirect(url.url_full)


class UrlCreateView(LoginRequiredMixin, CreateView):
    model = Url
    success_url = 'urls/list'
    form_class = UrlsForm
    template_name = 'url/url_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_login_url(self):
        login_url = '//app.localtest.me:8000/login/'
        return str(login_url)


class UrlListView(LoginRequiredMixin, ListView):
    model = Url
    context_object_name = 'urls'
    template_name = 'url/urls_list.html'


    def get_login_url(self):
        return '//app.localtest.me:8000/login/'

    def get_queryset(self):
        return self.request.user.url.all()


class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'
    template_name = 'url/url_detail.html'


class UrlUpdateView(UpdateView):
    model = Url
    success_url = '/urls/list'
    form_class = UrlsForm
    template_name = 'url/url_form.html'


class UrlDeleteView(DeleteView):
    model = Url
    success_url = '/urls/list'
    template_name = 'url/url_delete.html'
