
from django.db import models
from django.forms import ModelForm

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    date_of_birth = models.DateField(max_length=10)
    date_of_ordering=models.CharField(max_length=10)

    def __str__(self):
            return self.name

class Emails_only(models.Model):
    email = models.EmailField(max_length=150)
    date_of_ordering=models.CharField(max_length=10)

class SubscribeForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['date_of_ordering']
