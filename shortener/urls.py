from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UrlsShortified.as_view(), name='urls.list'),
]