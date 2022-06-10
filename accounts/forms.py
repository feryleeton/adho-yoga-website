from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}))
    first_name = forms.CharField(max_length=255, required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name', 'id': 'first_name'}))
    password1 = forms.CharField(max_length=255, required=True, label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password1'}))
    password2 = forms.CharField(max_length=255, required=True, label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'id': 'password2'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=15, required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(max_length=255, required=True, label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'id': 'password2'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
