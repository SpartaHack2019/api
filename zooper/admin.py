# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('id', 'image_tag', 'image', 'likes', 'dislikes', 'description', 'adoption', 'adoption_url', 'user')
    readonly_fields = ('id', 'image_tag',)