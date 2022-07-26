from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def signup(request):
    context = {}
    return render(signup, 'signup.html', context)
