

# from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm
from .models import Emails_only,Person,SubscribeForm
from django.core.mail import send_mail, BadHeaderError
from datetime import datetime
import time
from django.shortcuts import render, redirect


# @csrf_protect
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {'name': form.cleaned_data['name'],'phone_number': form.cleaned_data['phone_number'],'email': form.cleaned_data['email'],'date_of_birth': form.cleaned_data['date_of_birth']}
            print(body)
            name = form.cleaned_data['name']
            # subject=f'Клиент: {name}, Дата: {datetime.now()}'
            number = form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            date_of_birth=form.cleaned_data['date_of_birth']
            # message = "\n".join(body.values())
            date_of_ordering=datetime.now()
            p = Person(name=name, phone_number=number, email=email, date_of_birth=date_of_birth,date_of_ordering=date_of_ordering)
            email=Emails_only(email=email,date_of_ordering=date_of_ordering)
            email.save()
            p.save()  
            # return redirect('success')   
        print("хуй")      
    form = ContactForm()
    print('хуй2')
    return render(request, "contact_form/main.html", {'form': form})
        
    # form = SubscribeForm()
    # return render(request, "contact_form/Главная.html", {'form': form})
    # 
            # try:
            #     send_mail(subject,message,'vad.streltsov1001@yandex.ru',['vad.streltsov1001@yandex.ru'])
            # except BadHeaderError:
            #     print('Гавно случается')
        # else:
        #     print(f'\n-----------------------------\nform is valid={form.is_valid()}\n-----------------------------\n')    