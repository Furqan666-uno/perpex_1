from rest_framework import serializers
from django.contrib.auth import get_user_model # we need this to get AbstractUser from models.py
from .models import Order, Payment, Category, MenuItem
User= get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True, required=True)

    class Meta:
        model= User
        fields= ("username", "password", "role")

    def create(self, validated_data):
        user_data= User.objects.create_user(username= validated_data['username'], password= validated_data['password'], role= validated_data.get('role', 'Staff'))
        return user_data
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= ['id', 'product_name', 'amount', 'created_at']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "order", "amount", "status", "created_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ['id', 'name']


class MenuItemSerializer(serializers.ModelSerializer):
    category= CategorySerializer(read_only=True)

    class Meta:
        model= MenuItem
        fields= ['id', 'name', 'price', 'category']