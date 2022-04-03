from django import forms
from .models import *

class loginform(forms.ModelForm):
    class Meta:
        model = signupform
        fields = ['email','password']