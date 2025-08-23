from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES= (
        ("Manager", "Manager"),
        ("Waiter", "Waiter"),
        ("Cashier", "Cashier"),
    )
    role= models.CharField(max_length=50, choices=ROLES, default='Staff')

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