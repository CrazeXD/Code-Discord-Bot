from http.client import HTTPResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from .models import Code
# Create your forms here.
# When you are creating your Project model, give it a field for the owner's username (probably a charField, max_length 150). You can get the user by calling user = get_user(request) from the django.contrib.auth function, and get the user's username by calling user.get_username()
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    tier = 0
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.tier = self.tier
        if commit:
            user.save()
        return user

class NewCodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ("name", "fileextension")
        unique_together = ['name', 'owner', 'fileextension']
    def add_owner(self, request):
        username = request.user.username
        username = username.lower()
        return username
    def save(self, request, commit=True):
        code = super(NewCodeForm, self).save(commit=False)
        code.name = self.cleaned_data['name']
        code.fileextension = self.cleaned_data['fileextension']
        code.owner = self.add_owner(request)
        if commit:
            code.save()
        return code
        