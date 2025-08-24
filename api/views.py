from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegistrationSerializer, OrderSerializer, PaymentSerializer, MenuItemSerializer
from .models import Order, Payment, User, MenuItem, Category
from .permissions import IsManager_Or_IsAdmin, IsWaiter, IsCashier
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
User= get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class= UserRegistrationSerializer    


class OrderView(APIView):
    permission_classes= [IsAuthenticated, IsWaiter]

    def get(self, request):
        orders= Order.objects.filter(user=request.user) # filter orders for logged-in user 
        serializer= OrderSerializer(orders, many=True)
        return Response(serializer.data) # shows all order of this user
        
    def post(self, request):
        if request.user.role != "Waiter":
            return Response({'error':'Only waiters can create orders'}, status=403)

        serializer= OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class PaymentView(APIView):
    permission_classes= [IsAuthenticated, IsCashier]

    def get(self, request):
        payments= Payment.objects.all()
        serializer= PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != "Cashier":
            return Response({'error':'Only cashier can take payments'}, status=403)
        
        serializer= PaymentSerializer(data=request.data)
        if serializer.is_valid():
            order= serializer.validated_data["order"]
            if order.user != request.user:
                return Response({'error':'Only cashier can take payments'}, status=403)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class MenuItemView(APIView):
    permission_classes= [IsAuthenticated, IsManager_Or_IsAdmin]

    def get(self, request):
        menu_items = MenuItem.objects.select_related("category").all() # selected_related= more efficient than simple .all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.role in ["Manager", "Admin"]:
            return Response({"error": "Only Manager and/or Admin can add dishes"}, status=403)
        
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    