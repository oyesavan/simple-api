import graphene
import gqlApi.schema
class Query(gqlApi.schema.Query, graphene.ObjectType):
    pass
class Mutation(gqlApi.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)