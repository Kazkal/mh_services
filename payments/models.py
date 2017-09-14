# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.
class Invoice(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    invoice_number=models.CharField(max_length=50, unique=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(auto_now_add=True)
    date_paid= models.DateTimeField(blank=True, null=True)

