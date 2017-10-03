# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import register, login, logout
from django.core.urlresolvers import resolve
from models import User
from forms import UserRegistrationForm, UserLoginForm
from django import forms
from django.conf import settings

#url(r'^register/$', accounts_views.register, name='register'),
# url(r'^login/$', accounts_views.login, name='login'),
class RegisterPageTest(TestCase):

    fixtures = ['blog', 'user']

    def test_register_page_resolves(self):
        register_page = resolve('/register/')
        self.assertEqual(register_page.func, register)

    # check status code so that page returns actual page
    def test_register_page_status_code_is_ok(self):
        register_page = self.client.get('/register/')
        self.assertEqual(register_page.status_code, 200)

    #check content and template used
    # output of template from URL is same as when use render_to_response to directly render its output locally.

class LoginPageTest(TestCase):
    def test_login_page_resolves(self):
        login_page = resolve('/login/')
        self.assertEqual(login_page.func, login)

    # check status code so that page returns actual page
    def test_login_page_status_code_is_ok(self):
        login_page = self.client.get('/login/')
        self.assertEqual(login_page.status_code, 200)

#  url(r'^logout/$', accounts_views.logout, name='logout'),
class LogoutPageTest(TestCase):
    def test_logout_page_resolves(self):
        logout_page = resolve('/logout/')
        self.assertEqual(logout_page.func, logout)

  #cannot check for status code as no logout page

#test for email given/not given:
class CreateUserTest(TestCase):
    def test_manager_create(self):
        user = User.objects._create_user(None, "model@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)

    #test register form with correct data:
    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'model33@test.com',
            'password1': 'tester33',
            'password2': 'tester33',
        })
        self.assertTrue(form.is_valid())

    #test register form with missing data:
    def test_registration_form_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'test35',
            'password2': 'test35',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    #test register form with passwords not matching:
    def test_registration_form_passwords_not_matching(self):
        form = UserRegistrationForm({
            'email': 'model38@test.com',
            'password1': 'tester38',
            'password2': 'tester39',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())



    #test register form for missing 2nd password:
    def test_registration_form_password_missing(self):
        form = UserRegistrationForm({
            'email': 'model40@test.com',
            'password1': 'tester40',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Second Password is missing",
                                 form.full_clean())

    # test 11 - test login form with correct data:
    def test_login_form(self):
        form = UserLoginForm({
            'email': 'model11@test.com',
            'password': 'tester11',
        })
        self.assertTrue(form.is_valid())

    # test 12 - test login form with missing email:
    def test_login_form_missing_email(self):
        form = UserLoginForm({
            'password': 'tester12',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Email address is missing",
                                 form.full_clean())

    # test 13 - test login form with missing password:
    def test_login_form_missing_password(self):
        form = UserLoginForm({
            'email': 'testcase13@test.com',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Password is missing",
                                 form.full_clean())




