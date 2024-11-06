from django.forms import ModelForm
from .models import CV, CVInfo
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


class CVInfoForm(ModelForm):
    class Meta:
        model = CVInfo
        fields = ['fullName', 'email', 'experienceYears', 'jobTitle', 'description', 'requirements']
        widgets = {
            'jobTitle' : forms.HiddenInput(),
            'description' : forms.HiddenInput(),
            'requirements' : forms.HiddenInput(),
        }