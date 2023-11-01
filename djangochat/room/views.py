from django.shortcuts import render

# import Room model
from .models import Room

# importing login func for security 
from django.contrib.auth.decorators import login_required

# rooms
@login_required
def rooms(request):
    # defining rooms
    rooms = Room.objects.all()

    return render( request , "room/rooms.html" , {
        'rooms': rooms
    })

# room
@login_required
def room(request , slug):
    # object Room
    room = Room.objects.get(slug=slug)
    return render( request , "room/room.html" , {
        'room': room
    })