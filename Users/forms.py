from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

#user register form
class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]