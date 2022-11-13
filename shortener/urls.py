from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('list/', views.UrlListView.as_view(), name='urls.list'),
    path('list/<int:pk>', views.UrlDetailView.as_view(), name='url.detail'),
    path('list/<int:pk>/edit', views.UrlUpdateView.as_view(), name='url.update'),
    path('list/<int:pk>/delete', views.UrlDeleteView.as_view(), name='url.delete'),
    path('new/', views.UrlCreateView.as_view(), name='url.new'),
]
