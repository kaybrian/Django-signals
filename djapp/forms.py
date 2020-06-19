from django import forms 
from django.forms import ModelForm
from .models import * 


class numbersinc(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['number',]