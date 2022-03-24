import email
from django.db import models
from django.forms import EmailField


class PharmacyAdmin(models.Model):
    email = models.EmailField()
    password = models.TextField()
