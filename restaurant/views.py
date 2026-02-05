# django imports
from django.shortcuts import render
from django.contrib.auth.models import User

# REST Framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

# local imports
from .forms import BookingForm
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer


# static view for home page landing
def home(request):
    return render(request, "index.html")


# static view for about page
def about(request):
    return render(request, "about.html")


# static view for booking page
def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


# static view for menu page
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


# static view for individual menu item page
def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


# API viewset for User
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# API viewset for Booking
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Success!", "data": serializer.data})
        return Response(serializer.errors, status=400)


# API view for Menu Items
class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = []

    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Success!", "data": serializer.data})
        return Response(serializer.errors, status=400)


# API view for Single Menu Item
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = []

    def get(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found!"}, status=404)

        serializer = MenuSerializer(menu_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found!"}, status=404)

        serializer = MenuSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Success!", "data": serializer.data})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found!"}, status=404)

        menu_item.delete()
        return Response({"status": "Success!", "message": "Menu item deleted!"})
