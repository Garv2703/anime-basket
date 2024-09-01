from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User


# Create your forms here.
class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email):
            raise forms.ValidationError(("This email address is already in use. Please supply a different email address."))
        return email

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))