from django import forms
from .models import Url

class UrlsForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url_full',)
        labels = {
            'url_full': 'url to shortify'
        }
