# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.
def list_posts(request):
    return render(request, "blog/blog_posts.html", {'vposts': Post.objects.all()})


