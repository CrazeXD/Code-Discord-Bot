from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def signup(request):

    return render(request, 'signup.html', {})
    
def home(request):
    context = {}
    return render(request, 'home.html', context)
