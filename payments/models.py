# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

# Create your models here.
class Invoice(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    invoice_number=models.CharField(max_length=50, unique=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(auto_now_add=True)
    date_paid= models.DateTimeField(blank=True, null=True)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.amount,
            "currency": "EUR",
            "item_name": self.user_id,
            "invoice": self.invoice_number,
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name

