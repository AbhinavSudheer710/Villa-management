from django.db import models

# Create your models here.
class Property_Detailss(models.Model):
    property_photo=models.ImageField()
    builder_id=models.CharField(max_length=200)
    property_category=models.CharField(max_length=200)
    property_name=models.CharField(max_length=200)
    property_location=models.CharField(max_length=200)
    property_budget=models.CharField(max_length=200)
    bedrooms=models.CharField(max_length=200)
    bathrooms=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    floor=models.CharField(max_length=200)
    parking=models.CharField(max_length=200)