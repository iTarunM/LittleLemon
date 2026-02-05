from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.decorators import api_view, permission_classes

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer


def index(request):
    return render(request, "index.html", {})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def secure_view(request):
    return Response({"message": "needs authentication"})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


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
            return Response({"status": "success", "data": serializer.data})
        return Response(serializer.errors, status=400)


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response(serializer.errors, status=400)


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=404)

        serializer = MenuSerializer(menu_item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=404)

        serializer = MenuSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=404)

        menu_item.delete()
        return Response({"status": "success", "message": "Menu item deleted"})
