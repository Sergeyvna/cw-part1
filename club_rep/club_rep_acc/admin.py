from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(ClubRep)
admin.site.register(Club)
admin.site.register(Films)
admin.site.register(Booking)