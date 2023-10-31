from .views import frontpage , signup
from django.urls import path

# log func import
from django.contrib.auth import views as auth_views

urlpatterns = [
    # normal path
    path('', frontpage , name="frontpage"),

    # sign up path
    path('signup/', signup , name="signup"),

    # logout url
    path('logout/' , auth_views.LogoutView.as_view() , name="logout"),

    # login url
    path('login/' , auth_views.LoginView.as_view() , name="login")
]
