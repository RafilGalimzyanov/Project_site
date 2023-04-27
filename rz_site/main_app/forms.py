from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'id': 'floatingInput', 'name': 'email', 'placeholder': 'name@example.com', }))
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'floatingName', 'name': 'Имя', 'placeholder': 'name', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'floatingPassword1', 'name': 'password1', 'placeholder': 'Password', }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'floatingPassword2', 'name': 'password2', 'placeholder': 'Password', }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'floatingInput', 'name': 'email', 'placeholder': 'name', }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'floatingPassword', 'name': 'password', 'placeholder': 'Password', }))


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rev', ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rev': forms.Textarea(attrs={'class': 'form-control h-25'}),
        }