from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import AdhoUser


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
        model = AdhoUser
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
        model = AdhoUser
        fields = [
            'username',
            'password'
        ]


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name', 'id': 'first_name', 'type': 'text'}))
    last_name = forms.CharField(max_length=50, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name', 'id': 'last_name', 'type': 'text'}))
    username = forms.CharField(max_length=50, required=True, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username', 'type': 'text'}))
    email = forms.CharField(max_length=50, required=False, label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email address', 'id': 'email_address', 'type': 'email'}))
    mobile_number = forms.CharField(max_length=50, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone', 'id': 'phone', 'type': 'text'}))
    country = forms.CharField(max_length=50, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Country', 'id': 'country', 'type': 'text'}))
    state = forms.CharField(max_length=50, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'State', 'id': 'state', 'type': 'text'}))
    address = forms.CharField(max_length=50, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Address', 'id': 'address', 'type': 'text'}))
    postal_code = forms.CharField(max_length=50, required=False, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Postal Code', 'id': 'postal_code', 'type': 'text'}))

    class Meta:
        model = AdhoUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'country',
            'state',
            'address',
            'postal_code',
            'mobile_number',
        ]
