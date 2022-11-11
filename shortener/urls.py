from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.UrlList.as_view(), name='urls.list'),
    path('detail/<int:pk>', views.UrlDetail.as_view(), name='url.detail')
]