# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .views import get_home
from accounts.models import User
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

# Create your tests here.
class HomePageTest(TestCase):

    #fixtures = ['blog', 'user']
    #create 1 user instead
    def setUp(self):
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testerKK')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testerKK',
                                       password='letmein')
        self.assertEqual(self.login, True)

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_home)

    #check status code so that page returns actual page
    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    #check content & template used
    def test_home_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "home.html")
        home_page_template_output = render_to_response("home.html", {'user':self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)