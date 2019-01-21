from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text='Optional.')
    last_name = forms.CharField(max_length=30, help_text='Optional.')
    email = forms.EmailField(max_length=500)
    password1 = forms.CharField(max_length=30, help_text='Optional.')
    password2 = forms.CharField(max_length=30, help_text='Optional.')
    location = forms.CharField(max_length=30, help_text='Optional.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','location' )


