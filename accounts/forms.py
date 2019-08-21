from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


# Create a new form object
class UserLoginForm(forms.Form):
    '''
    Form to be used to log users in
    '''
    username = forms.CharField()
    # widget of password input ensures field has input type of password
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    '''
    Form used to create a new user
    '''
    # First password entry
    password = forms.CharField(widget=forms.PasswordInput)
    # Confirm password with a label
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput)
    # Create inner class to give more info about fomr - model and fields
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
