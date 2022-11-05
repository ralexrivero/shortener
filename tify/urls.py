from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from . import views

urlpatterns = [
        path('greet/', views.greet, name='greet'),
]
