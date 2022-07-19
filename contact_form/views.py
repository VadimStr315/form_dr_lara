# from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm
from .models import Emails_only,Person,SubscribeForm
from django.core.mail import send_mail, BadHeaderError
from datetime import datetime
import time
from django.shortcuts import render, redirect
import requests
import json
def success(request):
    # if request.method == 'GET': 
    #     return redirect('form')
    return render(request,"contact_form/success.html")


# @csrf_protect
def contact(request):
    if request.method == 'GET': 
        form = SubscribeForm() 
        
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            body = {'name': form.cleaned_data['name'],'phone_number': form.cleaned_data['phone_number'],'email': form.cleaned_data['email'],'date_of_birth': str(form.cleaned_data['date_of_birth'])}
            print(body)
            name = form.cleaned_data['name']
            number = form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            date_of_birth=form.cleaned_data['date_of_birth']
            date_of_ordering=datetime.now()
            p = Person(name=name, phone_number=number, email=email, date_of_birth=str(date_of_birth),date_of_ordering=date_of_ordering)
            email=Emails_only(email=email,date_of_ordering=date_of_ordering)
            email.save()
            p.save()  

            return redirect('/success',foo='bar')  
            # return render(request,"contact_form/success.html")

        else: 
            print(form.errors) 
            # return render(request,f"<h1>{form.errors}<h1>")
     
    form = SubscribeForm()
    
    return render(request, "contact_form/main.html", {'form': form})
