from django.shortcuts import render
from .forms import Signup

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def signup(request):
    context = {}
    context['form'] = Signup()
    return render(request, "signup.html", context)