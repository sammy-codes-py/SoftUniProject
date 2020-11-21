from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from user.models import ProfileUser


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        exclude = ['user']
