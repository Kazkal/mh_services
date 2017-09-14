# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here. Access to blog restricted to registered users
@login_required(login_url='/login/')
def list_posts(request):
    return render(request, "blog/blog_posts.html", {'vposts': Post.objects.all()})

def post_detail(request, id):
    """
    view to return 1 Post  based on the post ID Or return a 404 error if post not found
    """
    vpost = get_object_or_404(Post, pk=id)
    return render(request, "blog/blog_detail.html", {'post': vpost})


