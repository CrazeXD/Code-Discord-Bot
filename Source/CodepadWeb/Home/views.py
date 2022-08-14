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
    objects = Code.objects.filter(owner__exact=username).order_by("last_edit")[:5]
    objects = list(objects)
    context = {"Username": username, "codes": objects}
    return render(request, "home.html", context)

@login_required(login_url="/login")
def create(request):
    if request.method == "POST":
        form = NewCodeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] not in [project.name for project in Code.objects.filter(owner__exact=request.user.username)]:
                code = form.save(request, commit=False)
                code.codefile = DEFAULT_FOR_LANG[form.cleaned_data['fileextension']]
                code.save(request)
            return HttpResponseRedirect(f"/edit/{request.user.username}/{form.cleaned_data['name']}/")
    else:
        form = NewCodeForm()
        return render(request, "create.html", {"create_form": form})

def edit(request, username, name):
    if request.user.username==username and request.user.is_authenticated:
        code = Code.objects.filter(owner=username, name=name)
        code = code[0]
        text = code.codefile
        context = {'title': name, "code": text}
        return render(request, 'edit.html', context)
    return HttpResponse("You are not authorized to view this page.")