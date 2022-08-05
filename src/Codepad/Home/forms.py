from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
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