# danjgo imports
from django.test import TestCase

# local imports
from restaurant.models import Booking, Menu


# test Menu model
class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            name="Pasta",
            price=12.5,
            menu_item_description="Delicious pasta with tomato sauce",
        )
        self.assertEqual(str(item), "Pasta")


# test Booking model
class BookingModelTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(
            name="Alice", no_of_guests=4, booking_date="2024-07-01"
        )
        self.assertEqual(str(booking), "Alice")
