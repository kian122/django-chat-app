from .views import frontpage , signup
from django.urls import path

urlpatterns = [
    # normal path
    path('', frontpage , name="frontpage"),

    # sign up path
    path('signup/', signup , name="signup"),
]
