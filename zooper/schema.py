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

class CreatePost(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        description = graphene.String()
        adoption = graphene.Boolean()
        adoption_url = graphene.String()

    def mutate(self, info, description, file1, adoption_url):
        post = Post(description=description, 
                    adoption_url=adoption_url)
        # image stuff here
        post.save()
        return CreatePost(success=True)

class LikePost(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        post_id = graphene.String()

    def mutate(self, info, post_id):
        post = Post.objects.get(id=post_id)
        post.likes = post.likes + 1
        post.save()
        return LikePost(success=True)

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    posts = graphene.Field(PostPaginatedType, page=graphene.Int())

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()
    
    def resolve_posts(self, info, page):
        page_size = 10
        qs = Post.objects.all()
        return get_paginator(qs, page_size, page, PostPaginatedType)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    like_post = LikePost.Field()