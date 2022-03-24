from django.db import models
from sellers.models import Product


class Users(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.TextField()


class prof(models.Model):
    name = models.TextField(max_length=50)
    phone = models.TextField()
    address = models.TextField(max_length=100)
    img = models.ImageField(upload_to='products')


class Order(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    cust = models.ForeignKey(Users, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=30, default="added to cart")
