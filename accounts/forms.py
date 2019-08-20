from django import forms


# Create a new form object
class UserLoginForm(forms.Form):
    '''
    Form to be used to log users in
    '''
    username = forms.CharField()
    # widget of password input ensures field has input type of password
    password = forms.CharField(widget=forms.PasswordInput)