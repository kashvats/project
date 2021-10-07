from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.validators import ValidationError
from django.core import validators



class signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class amri(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    # def clean(self):
    #     super().clean()
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')
    #
    #     if User.objects.filter(username=username).exists():
    #         raise ValidationError('Username already exist,please choose another one')
    #
    #     elif User.objects.filter(email=email).exists():
    #         raise ValidationError('email already exist')


class teacherplus(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['tname','subject','address','mobile']

class studentplus(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','classe','roll','mother','father','address','mobile']