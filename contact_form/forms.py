from django import forms
from django.db import models
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    date_of_birth = forms.CharField(max_length=10)

