from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from main.models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone', 'id': 'phone', 'type': 'tel'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message...',
                'id': 'message',
                'cols': 30,
                'rows': 7,
            }),
        }