# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Portfolio(models.Model):
    """
    Here we'll define our Portfolio model
    """
    # portfolio can be linked to a registered user, via the User model in the accounts app
    #customer_id= models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

class Testimonial(models.Model):
    testimonial = models.CharField(max_length=254)
    #name comes from user table, linking on user_id
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    location = models.CharField(max_length=254)





