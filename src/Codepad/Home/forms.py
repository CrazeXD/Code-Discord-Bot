from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
# Create your forms here.

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
#https://pypi.org/project/django-currentuser/
