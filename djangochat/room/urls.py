from django.urls import path 

# import views func
from .views import rooms , room

urlpatterns = [
    # all rooms url
    path( '', rooms , name="rooms"),

    #detail room url
    path( '<slug:slug>/', room , name="room"),
]
