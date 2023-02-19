from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings

def home_view(request):
    
        
    return render(request,'index.html')

def design(request):
    products=models.Product.objects.all()
        
    return render(request,'design.html',{'products':products})

def blog(request):
    blog=models.Blog.objects.all()
        
    return render(request,'blog.html',{'blog':blog})



def aboutus_view(request):
    return render(request,'aboutus.html')

