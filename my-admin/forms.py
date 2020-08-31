from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class AdminUserForm(forms.Form):

    is_staff = forms.BooleanField(required=False, initial=False)
    is_active = forms.BooleanField(required=False, initial=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'department',
            'is_active',
            'is_staff'

        ]

