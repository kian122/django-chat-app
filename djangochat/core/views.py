from django.shortcuts import render , redirect

# importing all the forms
from . import form

# importing login function
from django.contrib.auth import login

# Create your views here.

def frontpage(request):
    return render( request , "core/frontpage.html" )