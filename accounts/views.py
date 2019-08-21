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
    # If request method is POST, we want to validate login details
    if request.method == "POST":
        # Create an instance of login form and pass POST request as constructor
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            # If form is valid, we get both entered username and password
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                # If details are valid, log user in and display message
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
            else:
                # If details don't match, display error message
                login_form.add_error(None, 'Your username or password is \
                                     incorrect!')

    else:
        # Else, we want to return a blank form
        login_form = UserLoginForm()

    return render(request, "login.html", {"login_form": login_form})
