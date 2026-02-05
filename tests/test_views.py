from django.test import TestCase
from django.contrib.auth.models import User


class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_get_menu_items(self):
        self.client.force_login(self.user)
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)

    def test_post_menu_item(self):
        self.client.force_login(self.user)
        data = {"title": "Pasta", "price": 12.5, "inventory": 10}
        response = self.client.post("/restaurant/menu/", data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json()["data"])


class BookingViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_get_bookings(self):
        self.client.force_login(self.user)
        response = self.client.get("/restaurant/booking/tables/")
        self.assertEqual(response.status_code, 200)

    def test_post_booking(self):
        self.client.force_login(self.user)
        data = {"name": "Alice", "no_of_guests": 4, "booking_date": "2024-07-01"}
        response = self.client.post("/restaurant/booking/tables/", data)
        self.assertEqual(response.status_code, 201)


class SingleMenuItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_login(self.user)
        self.menu_item = {"title": "Pasta", "price": 12.5, "inventory": 10}
        response = self.client.post("/restaurant/menu/", self.menu_item)
        self.menu_item_id = response.json()["data"]["id"]

    def test_get_single_menu_item(self):
        response = self.client.get(f"/restaurant/menu/{self.menu_item_id}/")
        self.assertEqual(response.status_code, 200)

    def test_update_single_menu_item(self):
        updated_data = {"title": "Spaghetti", "price": 15.0, "inventory": 8}
        response = self.client.put(
            f"/restaurant/menu/{self.menu_item_id}/",
            updated_data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_single_menu_item(self):
        response = self.client.delete(f"/restaurant/menu/{self.menu_item_id}/")
        self.assertEqual(response.status_code, 200)


class UserRegistrationTest(TestCase):
    def test_register_user(self):
        data = {"username": "newuser", "password": "testpass123"}
        response = self.client.post("/auth/users/", data)
        self.assertEqual(response.status_code, 201)
