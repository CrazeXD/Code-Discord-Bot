import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from .models import Code

DEFAULT_FOR_LANG = {
    "py": "print(\"Hello world!\")",
    "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n\tcout << \"Hello world!\" << endl;\n}",
    "java": "class Main {\n\tpublic static void Main(String[] args) {\n\t\tSystem.out.println(\"Hello world!\");\n\t}]n}",
    "c": '''#include <stdio.h>
            int main() {
            \tprintf("Hello, World!");
            return 0;
            }
        ''',
    "js": "console.log('Hello World');"        
}


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
    objects = Code.objects.filter(owner__exact=username.lower()).order_by("last_edit")[:5]
    objects = list(objects)
    context = {"Username": username, "codes": objects}
    return render(request, "home.html", context)

@login_required(login_url="/login")
def create(request):
    if request.method == "POST":
        form = NewCodeForm(request.POST)
        if form.is_valid():
            code = form.save(request, commit=False)
            code.owner = request.user.username
            code.codefile = DEFAULT_FOR_LANG[form.cleaned_data['fileextension']]
            code.save(request)
            return HttpResponseRedirect(f"{request.user.id}/{form.cleaned_data['name']}/")
    else:
        form = NewCodeForm()
        return render(request, "create.html", {"create_form": form})