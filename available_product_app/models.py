from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    boutique = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reserved_time = models.DateTimeField()
    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=True)  # blank=True permet que le champ soit laissé vide
    phone_number = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    desired_quantity = models.CharField(max_length=255)
