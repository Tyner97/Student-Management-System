import graphene
from trade.queries import Query as TradeQuery
from trade.mutations import Mutation as TradeMutation


class Query(TradeQuery, graphene.ObjectType):
    pass


class Mutation(TradeMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
