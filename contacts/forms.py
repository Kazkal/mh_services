from django import forms
from .models import Contact

class ContactAddForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'enquiry','postcode')


