from django.urls import path 

# import views func
from .views import rooms

urlpatterns = [
    path( "" , rooms , name="rooms"),
]
