"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# django imports
from django.contrib import admin
from django.urls import path, include

# REST framework imports
from rest_framework.routers import DefaultRouter

# local imports
from restaurant.views import BookingViewSet

# router creation and registering viewsets with it
router = DefaultRouter()
router.register(r"tables", BookingViewSet, basename="booking")

# URL patterns for the project
urlpatterns = [
    # Django admin site
    path("admin/", admin.site.urls),
    # Authentication URLs provided by Djoser
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    # Authentication URLs provided by Django REST framework
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # include URLs from the restaurant app
    path("restaurant/", include("restaurant.urls")),
    # API endpoint for the restaurant booking app
    path("restaurant/booking/", include(router.urls)),
]
