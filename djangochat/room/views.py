from django.shortcuts import render

# import Room model
from .models import Room

# importing login func for security 
from django.contrib.auth.decorators import login_required

@login_required
def rooms(request):
    # defining rooms
    rooms = Room.objects.all()

    return render( request , "room/rooms.html" , {
        'rooms': rooms
    })
    