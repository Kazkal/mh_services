# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import list_posts, post_detail
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response
from accounts.models import User

# Create your tests here.
# url(r'^blog/$', views.list_posts, name='blog'),
# url(r'^blog/(?P<id>\d+)/$', views.post_detail),
class BlogPageTest(TestCase):
    # create 1 user instead
    def setUp(self):
        super(BlogPageTest, self).setUp()
        self.user = User.objects.create(username='testerKK')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testerKK',
                                       password='letmein')
        self.assertEqual(self.login, True)

    def test_blog_page_resolves(self):
        blog_page = resolve('/blog/')
        self.assertEqual(blog_page.func, list_posts)

    #test page returns actual page, if login-required used then code 302 else 200
    def test_blog_page_status_code_is_ok(self):
        blog_page = self.client.get('/blog/')
        self.assertEqual(blog_page.status_code, 200)

    #checks on the content and the template that was used:if login-required then assertion error
    def test_blog_content_is_correct(self):
        blog_page = self.client.get('/blog/')
        self.assertTemplateUsed(blog_page, "blog/blog_posts.html")
        blog_page_template_output = render_to_response("blog/blog_posts.html", {'user':self.user}).content
        self.assertEqual(blog_page.content, blog_page_template_output)


class BlogDetailPageTest(TestCase):
    def test_detail_page_resolves(self):
        detail_page = resolve('/blog/2/')
        self.assertEqual(detail_page.func, post_detail)

    # test page returns actual page
    def test_detail_page_status_code_is_ok(self):
        detail_page = self.client.get('/blog/2')
        self.assertEqual(detail_page.status_code, 301)

    #checks on the content and the template that was used:
    def test_detail_content_is_correct(self):
        detail_page = self.client.get('/blog/2')
        self.assertTemplateUsed(detail_page, "blog/blog_detail.html")
        detail_page_template_output = render_to_response("blog/blog_detail.html").content
        self.assertEqual(detail_page.content, detail_page_template_output)





