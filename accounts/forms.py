from django import forms
from .models import User


class UserForm(forms.modelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
