from django.contrib import admin

# Room model
from .models import Room , Message


#registering Room
admin.site.register(Room)
admin.site.register(Message)