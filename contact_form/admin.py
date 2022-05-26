from django.contrib import admin
from contact_form.models import Person,Emails_only

@admin.register(Emails_only)
class AdminEmail(admin.ModelAdmin):
    list_display = ("email","date_of_ordering")

@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ("name","phone_number","email","date_of_birth","date_of_ordering")
    # list_filter =("name","phone_number","email","date_of_birth","date_of_ordering")