# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Portfolio

# url(r'^portfolio/', portfolio_views.get_portfolios, name='portfolio'),
class PortfolioPageTest(TestCase):
    def test_portfolio_content_is_correct(self):
        portfolio_page = self.client.get('/portfolio/')
        self.assertTemplateUsed(portfolio_page, "portfolios/portfolios.html")
        portfolio_page_template_output = render_to_response("portfolios/portfolios.html",
                                                          {'portfolios':
                                                               Portfolio.objects.all()}).content
        self.assertEqual(portfolio_page.content, portfolio_page_template_output)