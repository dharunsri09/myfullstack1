from django.contrib import admin

# Register your models here.

from .models import VacCenter,Booked,Bookings,MyModel

admin.site.register(VacCenter)
admin.site.register(Booked)
admin.site.register(Bookings)
admin.site.register(MyModel)