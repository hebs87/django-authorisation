from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.
def index(request):
    '''
    Return the index.html file
    '''
    return render(request, "index.html")


def logout(request):
    '''
    Log the user out
    '''
    auth.logout(request)
    # Display a flash message when user is logged out
    messages.success(request, "You have successfully been logged out!")
    # Reverse allows to redirect to url name rather than html file or function
    return redirect(reverse('index'))


def login(request):
    '''
    Return a login page
    '''
    # Create instance of the login form
    login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
