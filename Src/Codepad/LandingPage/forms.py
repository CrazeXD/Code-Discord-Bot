from django import forms
import re
class Signup(forms.Form):
    def validate(self, email):
        validemails = re.compile(re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2, 6})$', re.IGNORECASE))
        valid = validemails.fullmatch(email)
        return valid
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput())
    