import graphene
from graphene_django import DjangoObjectType
from .models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero

class Query(graphene.ObjectType):
    heroes = graphene.List(HeroType)
    hero = graphene.Field(HeroType, id= graphene.Int())
    def resolve_heroes(self, info, **kwargs):
        return Hero.objects.all()
    def resolve_hero(self, info, **kwargs):
        cur = kwargs.get('id')
        return Hero.objects.get(pk=cur)
