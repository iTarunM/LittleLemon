# django imports
from django.contrib import admin

# local imports
from .models import Booking, Menu

# registering models to the admin site
admin.site.register(Booking)
admin.site.register(Menu)
