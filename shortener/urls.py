from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('list/', views.UrlListView.as_view(), name='urls.list'),
    path('detail/<int:pk>', views.UrlDetailView.as_view(), name='url.detail'),
    path('new/', views.UrlCreateView.as_view(), name='url.new'),
]
