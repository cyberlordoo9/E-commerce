from django import forms
from .models import UserProfile # make sure this matches your actual model name


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'password']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'email', 'first_name', 'last_name']
