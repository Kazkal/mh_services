# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def payment_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'payments/payment_return.html', args)


def payment_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'payments/payment_cancel.html', args)
