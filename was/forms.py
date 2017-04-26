from django.forms import ModelForm
from was.models import User, Exercises

from django import forms

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['userID',
        'username',
        'age',
        'gender',
        'bodyWeight',
        'userLevel',
        'squatMax',
        'benchMax',
        'deadliftMax',
        'snatchMax',
        'cleanMax',
        'goals']
        

