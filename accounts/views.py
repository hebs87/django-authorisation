from django.shortcuts import render, redirect, reverse
from django.contrib import auth

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
    # Reverse allows to redirect to url name rather than html file or function
    return redirect(reverse('index'))