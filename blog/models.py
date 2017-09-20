# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    created_date = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    # link a new blog post to a registered user,
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title
