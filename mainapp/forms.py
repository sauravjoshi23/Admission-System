from django import forms
from .models import *

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