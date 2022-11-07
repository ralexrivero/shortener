from django.shortcuts import get_object_or_404, redirect

from .models import Url


def root(request, url_hash):
    url = get_object_or_404(Url, url_hash=url_hash)
    url.visited()

    return redirect(url.url_full)
