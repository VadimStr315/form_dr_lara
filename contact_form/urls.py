from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.contact,name='form'),
    path('success/',views.success,name='suсcess')
]