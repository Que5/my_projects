from django import forms
from .models import User


class UserForm(forms.modelForm):
    class Meta:
        model = User
