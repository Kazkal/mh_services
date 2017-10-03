# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .forms import ContactAddForm
from django import forms
from django.conf import settings

# Create your tests here.'full_name', 'email', 'enquiry')
class ContactTest(TestCase):

    def test_contact_form(self):
        form = ContactAddForm({
            'full_name': 'Tester Man',
            'email': 'TesterMan@gmail.com',
            'enquiry': 'Please quote for boiler service',
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_missing_email(self):
        form = ContactAddForm({
            'full_name': 'Tester Boy',
            'enquiry': 'Please quote for boiler repair',
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())