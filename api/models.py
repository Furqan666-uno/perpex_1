from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES= (
        ("Manager", "Manager"),
        ("Waiter", "Waiter"),
        ("Cashier", "Cashier"),
        ("Admin", "Admin"),
    )
    role= models.CharField(max_length=50, choices=ROLES, default='Waiter')

    def __str__(self):
        return self.username
    

class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product_name= models.CharField(max_length=100)
    amount= models.DecimalField(max_digits=5, decimal_places=2)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.product_name} for {self.user.username}")
    

class Payment(models.Model):
    ORDER_STATUS= (
        ("Pending", "Pending"),
        ("Successful", "Successful"),
        ("Failed", "Failed"),
    )
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount= models.DecimalField(max_digits=5, decimal_places=2)
    status= models.CharField(choices=ORDER_STATUS, default="Pending")
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Status for {self.order.product_name} is {self.status}')
    

class Category(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    name= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} is in {self.category.name}"