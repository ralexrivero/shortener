from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.views.generic.edit import DeleteView
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .forms import UrlsForm
from .models import Url


def root(request, url_hash):
    url = get_object_or_404(Url, url_hash=url_hash)
    url.visited()

    return redirect(url.url_full)


class RedirectHome(TemplateView):
    def redirect_home():
        return redirect(reverse('home', host='app'))


class UrlCreateView(LoginRequiredMixin, CreateView):
    model = Url
    success_url = 'urls/list'
    form_class = UrlsForm
    template_name = 'url/url_form.html'

    def get_login_url(self):
        login_url = 'http://admin.localhost:8000'
        return str(login_url)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UrlListView(LoginRequiredMixin, ListView):
    model = Url
    form_class = UrlsForm
    template_name = 'url/urls_list.html'

    def get_login_url(self):
        login_url = 'http://admin.localhost:8000'
        return str(login_url)

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)


class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'
    template_name = 'url/url_detail.html'


class UrlUpdateView(UpdateView):
    model = Url
    success_url = 'urls/list'
    form_class = UrlsForm
    template_name = 'url/url_form.html'


class UrlDeleteView(DeleteView):
    model = Url
    success_url = 'urls/list'
    template_name = 'url/url_delete.html'
