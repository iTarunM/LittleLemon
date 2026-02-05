# django imports
from django.contrib.auth.models import User

# REST Framework imports
from rest_framework import serializers

# local imports
from .models import Booking, Menu


# Booking serializer with custom choice field
class BookingSerializer(serializers.ModelSerializer):
    no_of_guests = serializers.ChoiceField(choices=[(i, i) for i in range(1, 7)])

    class Meta:
        model = Booking
        fields = "__all__"


# Menu serializer
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
