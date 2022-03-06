import email
from django.db import models


class Users(models.Model):
    name=models.TextField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.TextField()
    

class prof(models.Model):
    name=models.TextField(max_length=50)
    phone=models.TextField()
    address=models.TextField(max_length=100)
    img=models.ImageField(upload_to='products')
    