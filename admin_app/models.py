from django.db import models

# Create your models here.
class builder_details(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class builder_approve(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class booking(models.Model):
    property_name = models.CharField(max_length=200)
    property_location = models.CharField(max_length=200)
    property_price = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    