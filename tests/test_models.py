from django.test import TestCase
from restaurant.models import Booking, Menu


class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pasta", price=12.5, inventory=10)
        self.assertEqual(str(item), "Pasta")


class BookingModelTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(
            name="Alice", no_of_guests=4, booking_date="2024-07-01"
        )
        self.assertEqual(str(booking), "Alice")
