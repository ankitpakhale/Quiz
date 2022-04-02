from django import forms
from .models import *

class loginform(forms.ModelForm):
    class Meta:
        model = registerform
        fields = ['email','password']