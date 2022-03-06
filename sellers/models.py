from ast import Delete
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.forms import ImageField


class Sellers(models.Model):
    shop_name=models.TextField(max_length=50)
    seller_email=models.EmailField(unique=True)
    seller_password=models.TextField()
    med_img=ImageField()
    status=models.TextField(max_length=50, default="Not activated")

class Product(models.Model):
    fid=models.ForeignKey(Sellers, on_delete=models.CASCADE, null=True)
    med_name=models.TextField(max_length=300)
    price=models.TextField()
    quantity=models.TextField()
    description=models.TextField(max_length=500)
    med_img=models.ImageField()