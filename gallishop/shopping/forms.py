from django.forms import ModelForm

from django.contrib.auth.models import User
from django.db import models
from django.forms import fields

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']