import graphene
from graphene_django import DjangoObjectType

from .models import Url

class UrlType(DjangoObjectType):
    class Meta:
        model = Url

class Query(graphene.ObjectType):
    urls = graphene.List(UrlType)

    def resolve_urls(self, info, **kwargs):
        return Url.objects.all()
