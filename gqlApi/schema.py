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


class HeroInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String()
    gender = graphene.String()
    alias = graphene.String()



class CreateHero(graphene.Mutation):
    class Arguments:
        input = HeroInput(required=True)

    ok = graphene.Boolean()
    hero = graphene.Field(HeroType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        hero_instance = Hero(name=input.name,
                             alias=input.alias,
                             gender=input.gender)
        hero_instance.save()
        return CreateHero(ok=ok, hero=hero_instance)

class UpdateHero(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required = True)
        input = HeroInput(required = True)

    ok = graphene.Boolean()
    hero = graphene.Field(HeroType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False

        hero_instance = Hero.objects.get(pk=id)
        if hero_instance:
            ok = True
            if input.name:
                hero_instance.name = input.name
            if input.alias:
                hero_instance.alias = input.alias
            hero_instance.save()
            return UpdateHero(ok=ok, hero=hero_instance)
        return UpdateHero(ok=ok, hero=None)


class Mutation(graphene.ObjectType):
    create_Hero = CreateHero.Field()
    update_Hero = UpdateHero.Field()
