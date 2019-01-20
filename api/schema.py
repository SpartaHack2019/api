import graphene

import zooper.schema

class Query(zooper.schema.Query, graphene.ObjectType):
    pass

class Mutation(zooper.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)