from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .models import TravelBlogPost        

def home_page(request):
    return render(request,'blog_app/home.html')


def index_page(request):
    return HttpResponse('Welcome to Index Page')  

@login_required(login_url='login')
def dashboard(request):
    return render(request,'blog_app/dashboard.html')

def blog_post(request,id):
    
    try:
        blog = TravelBlogPost.objects.get(id=id)

    except TravelBlogPost.DoesNotExist:
        return render(request,'blog_app/404.html',status = 404)
    
    return render(request,'blog_app/blog_detail.html',{'blog':blog})            

def blog_list(request):
    
    blogs = TravelBlogPost.objects.all()
    return render(request,'blog_app/blog_list.html',{'blogs':blogs})
    
def blog_detail(request,id):
    
    blog = TravelBlogPost.objects.get(id=id)
    return render(request,'blog_app/blog_detail.html',{'blog':blog})

      
             