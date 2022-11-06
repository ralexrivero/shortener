import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Url


class UrlType(DjangoObjectType):
    class Meta:
        model = Url


class Query(graphene.ObjectType):
    urls = graphene.List(UrlType, url=graphene.String(), first=graphene.Int(), skip=graphene.Int())

    def resolve_urls(self, info, url=None, first=None, skip=None, **kwargs):
        queryset =  Url.objects.all()

        if url:
            _filter = Q(url_full__icontains=url)
            queryset = queryset.filter(_filter)

        if first:
            queryset = queryset[:first]
        if skip:
            queryset = queryset[skip:]

        return queryset

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
