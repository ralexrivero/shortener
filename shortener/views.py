from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.views.generic.edit import DeleteView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django_hosts.resolvers import reverse


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
    form_class = UrlsForm
    success_url = 'urls/list'
    template_name = 'urls/url_new.html'

    def get_login_url(self):
        return 'admin:login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UrlListView(LoginRequiredMixin, ListView):
    model = Url
    form_class = UrlsForm
    template_name = 'urls/urls_list.html'

    def get_login_url(self):
        return 'admin:login'

    def get_queryset(self):
        return Url.objects.filter(user=self.request.user)


class UrlDetailView(DetailView):
    model = Url
    context_object_name = 'url'
    template_name = 'urls/url_detail.html'
