from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

def login(request):
    if request.method == "POST":
        print("POST")
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # login session 생성
            return redirect('index')
    else: # GET
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)