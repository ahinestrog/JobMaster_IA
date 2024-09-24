from django.forms import ModelForm
from .models import CV
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CVForm(ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'email', 'phone', 'address', 'education', 'experience', 'languages', 'prompt']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
