from django.contrib import admin

# Room model
from .models import Room


#registering Room
admin.site.register(Room)