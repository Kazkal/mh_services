# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    enquiry = models.TextField()
    postcode=models.CharField(max_length=10)
    date_entered=models.DateTimeField(auto_now_add=True)

