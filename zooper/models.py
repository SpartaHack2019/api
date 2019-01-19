# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    description = models.TextField()
    adoption = models.BooleanField(default=False)
    adoption_url = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description[:100]

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="300"/>' % self.image)
    image_tag.short_description = 'Image'