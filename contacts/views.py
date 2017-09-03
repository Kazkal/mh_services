# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .forms import ContactAddForm

# Create your views here.
#after saving contact details, show thank you form
def new_contact(request):
    if request.method == "POST":
        form = ContactAddForm(request.POST)
        if form.is_valid():
            vcontact = form.save(commit=False)
            vcontact.date_entered = timezone.now()
            vcontact.save()
            return render(request, 'contacts/thankyou.html')
    else:
        form = ContactAddForm()
    return render(request, 'contacts/contactaddform.html', {'form':form})


