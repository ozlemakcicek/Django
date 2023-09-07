from django.contrib import admin

# Register your models here.
from .models import Car
from .models import Reservation

# Register your models here.
admin.site.register(Car)
admin.site.register(Reservation)