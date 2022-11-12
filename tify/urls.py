from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from shortener.views import root

app_name = 'main'

urlpatterns = (
        path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
        path('<str:url_hash>/', root, name='root'),
        path('urls/', include('shortener.urls')),
)
