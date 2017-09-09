# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from portfolios.models import Portfolio

# Create your views here.
def get_home(request):
    return render(request, 'home.html', {'var_portfolios_list': Portfolio.objects.all()})





