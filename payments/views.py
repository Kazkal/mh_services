# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Invoice
from accounts.models import User
from django.contrib.auth.decorators import login_required

#get invoices for registered user only Or return a 404 error if the invoice is not found
@login_required(login_url='/login/')
def get_invoices(request):
    return render(request, "payments/payment2.html", {"invoices_list":Invoice.objects.all()})

@login_required(login_url='/login/')
def invoice_detail(request):
    """
    Create a view that return a single invoice for user logged on
    """
    reguser=request.user
    invoice = get_object_or_404(Invoice, user_id=reguser)
    return render(request, "payments/payment2.html", {'invoice_det': invoice})





