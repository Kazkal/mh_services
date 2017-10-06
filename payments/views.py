# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Invoice
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

#get invoices for registered user only Or return a 404 error if the invoice is not found
@login_required(login_url='/login/')
def get_invoices(request):
    return render(request, "payments/payment2.html", {"invoices_list":Invoice.objects.all()})

@login_required(login_url='/login/')
def invoice_detail(request):
    """Create a view that returns a single invoice for user logged on"""
    reguser=request.user
    #invoice = get_object_or_404(Invoice, user_id=reguser)
    #return render(request, "payments/payment2.html", {'invoice_det': invoice})
    try:
        invoice = Invoice.objects.get(user_id=reguser)
    except Invoice.DoesNotExist:
        #need js alert here
        messages.add_message(request, messages.INFO, 'No invoice found.')
        #messages.error(request, "No invoice found.")
        return redirect(reverse('home'))
    return render(request, "payments/payment2.html", {'invoice_det': invoice})



