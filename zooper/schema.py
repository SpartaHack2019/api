import graphene

from graphene_django import DjangoObjectType

from .models import Post
from .utils import get_paginator

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class PostPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    objects = graphene.List(PostType)

class Query(object):
    all_posts = graphene.List(PostType)
    posts = graphene.Field(PostPaginatedType, page=graphene.Int())

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()
    
    def resolve_posts(self, info, page):
        page_size = 10
        qs = Post.objects.all()
        return get_paginator(qs, page_size, page, PostPaginatedType)