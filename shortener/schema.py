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


class CreateUrl(graphene.Mutation):
    url = graphene.Field(UrlType)

    class Arguments:
        url_full = graphene.String()

    def mutate(self, info, url_full):
        url = Url(url_full = url_full)
        url.save()

        return CreateUrl(url=url)


class Mutation(graphene.ObjectType):
    create_url = CreateUrl.Field()
