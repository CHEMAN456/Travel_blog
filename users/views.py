from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register_user(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    context = {'form':form}    
    
    return render(request,'users/register.html',context)


def login_view(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid User, Try Again')
            return render(request, 'users/login.html')  # ← No redirect
        
        login(request, user)
        
        if user.is_superuser:
            messages.success(request, f'Welcome Super User {user.username}, you have been logged in successfully')
        else:
            messages.success(request, f'Welcome User {user.username}, you have been logged in successfully')
        
        return redirect('index/')  # Adjust this route if needed
    
    return render(request, 'users/login.html')

def logout_view(request):
    
    if request.method == 'POST':
        logout(request)
        messages.success(request,
                            f'You have been logged out successfully')
        return redirect('blog_app:home')
    
    return render(request,'users/logout.html')
        
        
                