import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from .models import Code
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
            return HttpResponseRedirect("/home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "signup.html", {"register_form":form})

def login_rq(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home")
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
                return HttpResponseRedirect("/home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", context={"login_form":form})

@login_required(login_url="/login")
def dashboard(request):
    context = {}
    username = request.user.username
    objects = Code.objects.filter(user__exact=username.lower()).order_by("last_edit")[:5]
    objects = list(objects)
    context = {"Username": username, "codes": objects}
    return render(request, "home.html", context)

@login_required(login_url="/login")
def create(request):
    #TODO: Set up view based on form created in forms.py that is linked to the model defined in models.py
    if request.method == "POST":
        form = NewCodeForm(request.POST)
        if form.is_valid() and form.cleaned_data.get("name") not in list(Code.objects.filter(user__exact=request.user.username.lower())):
            code = form.save()
            messages.success("Codepad creation succesful!")
            time.sleep(2)
            return HttpResponseRedirect(f"/{request.user.id}/{form.cleaned_data.get('name')}")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    code = NewCodeForm()
    
    return HttpResponse(r"Coming soon!")