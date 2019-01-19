# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import mimetypes

from .models import Post

def download_image(request, image_id):
    post = Post.objects.get(id=image_id)
    wrapper = FileWrapper(open(post.image.path))
    content_type = 'image/png'
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(post.image)
    response['Content-Disposition'] = "attachment; filename=%s" %  post.image
    return response