# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
