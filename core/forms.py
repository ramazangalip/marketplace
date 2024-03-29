from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Kullanıcı Adı',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Şifre',
        'class':'w-full py-4 px-6 rounded-xl'
        }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Kullanıcı Adı',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Email',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Şifre',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Şifreyi Onayla',
        'class':'w-full py-4 px-6 rounded-xl'
        }))