from django.conf import settings
from django_hosts import patterns, host
from django.contrib import admin

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'app', 'app.urls', name='app'),
    host(r'admin', admin.site.urls, name='admin'),
)