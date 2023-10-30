from django.shortcuts import render , redirect

# importing all the forms
from .form import SignUpForm

# importing login function
from django.contrib.auth import login

# Create your views here.

# home page
def frontpage(request):
    return render( request , "core/frontpage.html" )

# sign up
def signup( request):
    # logic
    if request.method == "POST":
        form =  SignUpForm( request.POST)

        if form.is_valid():
            user = form.save()
            login( request , user )

            # Redirecting
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render( request , "core/signup.html" , {
        "form": form
    })