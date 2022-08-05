import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .models import Code #To create a code, call Code.objects.create_code(user=str(), fileextension=str(), codefile=str())
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, "index.html", {})

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            #Need to fix this redirect
            time.sleep(2)
            return HttpResponseRedirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "signup.html", {"register_form":form})

def login_rq(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                time.sleep(2)
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", context={"login_form":form})

@login_required
def dashboard(request):
    username = request.user.id
    return render(request, "home.html", {})
