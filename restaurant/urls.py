# dango imports
from django.urls import path

# REST Framework imports
from rest_framework.authtoken.views import obtain_auth_token

# local imports
from . import views

# URL patterns for restaurant app
urlpatterns = [
    # static HTML localhost:8000/restaurant/
    path("", views.home, name="home"),
    # static HTML localhost:8000/restaurant/about/
    path("about/", views.about, name="about"),
    # static HTML localhost:8000/restaurant/book/
    path("book/", views.book, name="book"),
    # static HTML localhost:8000/restaurant/menu/
    path("menu/", views.menu, name="menu"),
    path("menu/<int:pk>/", views.display_menu_item, name="menu_item"),
    # API token authentication
    path("api-token-auth/", obtain_auth_token),
    # MenuItems and SingleMenuItem API endpoints
    path("api/menu/", views.MenuItemsView.as_view()),
    path("api/menu/<int:pk>/", views.SingleMenuItemView.as_view()),
]
