from django.forms import ModelForm
from was.models import User

from django import forms

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['userID',
        'username',
        'age',
        'gender',
        'bodyWeight',
        'squatMax',
        'benchMax',
        'deadliftMax',
         ]
        

