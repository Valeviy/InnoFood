from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    # class Meta:
    #     model = settings.AUTH_USER_MODEL
    #     fields = ["username", "email", "password"]

