from django.contrib import admin
from .models import Room, Computer

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    pass


