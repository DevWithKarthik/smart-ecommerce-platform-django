from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('SELLER', 'Seller'),
        ('DELIVERY', 'Delivery'),
        ('CUSTOMER', 'Customer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CUSTOMER'
    )
    
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"

class SellerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    business_name = models.CharField(max_length=200)

    gst_number = models.CharField(max_length=50)

    address = models.TextField()

    phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

class DeliveryProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    hub_name = models.CharField(max_length=200)

    hub_area_sqft = models.IntegerField()

    employees_count = models.IntegerField()

    phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hub_name