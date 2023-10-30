""" this is just for forms """

# importing the self user pre load django 
from django.contrib.auth.models import User

# importing the create user function
from django.contrib.auth.forms import UserCreationForm

# Sign up form 
class SignUpForm( UserCreationForm ):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

