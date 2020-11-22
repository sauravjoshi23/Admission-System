from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('name', 'percentage', 'status', 'number')


class ITForm(forms.ModelForm):
    class Meta:
        model = IT
        fields = ('name', 'percentage', 'status', 'number')
        

class MechanicalForm(forms.ModelForm):
    class Meta:
        model = Mechanical
        fields = ('name', 'percentage', 'status', 'number')


class ElectronicsForm(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = ('name', 'percentage', 'status', 'number')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
