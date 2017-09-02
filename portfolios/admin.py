# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from portfolios.models import Portfolio
from portfolios.models import Testimonial

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Testimonial)

