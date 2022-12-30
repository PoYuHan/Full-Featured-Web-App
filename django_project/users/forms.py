from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # The form will going to be saved in "User" model
        fields = ['username', 'email', 'password1', 'password2']
