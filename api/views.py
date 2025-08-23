from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegistrationSerializer, OrderSerializer, PaymentSerializer
from .models import Order, Payment, User
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
User= get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class= UserRegistrationSerializer    


class OrderView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request):
        orders= Order.objects.filter(user=request.user) # filter orders for logged-in user 
        serializer= OrderSerializer(orders, many=True)
        return Response(serializer.data) # shows all order of this user
        
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class PaymentView(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.filter(order__user=request.user)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.validated_data["order"]
            if order.user != request.user:
                return Response({"error": "You can only pay for your own orders"}, status=403)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    