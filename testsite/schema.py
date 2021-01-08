import graphene
import gqlApi.schema
class Query(gqlApi.schema.Query, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query)