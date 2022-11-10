from django.contrib import admin
from . import models


class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_full', 'url_hash', 'visits', 'date_created', 'user')


admin.site.register(models.Url, UrlAdmin)
