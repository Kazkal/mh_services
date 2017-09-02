# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Portfolio, Testimonial


def get_portfolios(request):
    return render(request, "portfolios/portfolios.html", {'var_portfolios_list': Portfolio.objects.all()})

def get_testimonials(request):
    return render(request, "portfolios/testimonials.html", {'var_testimonials_list': Testimonial.objects.all()})

