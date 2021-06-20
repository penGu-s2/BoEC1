from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
class ProductGroup(models.Model):
    catalog_id=models.ForeignKey(Catalog,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)    
class Product(models.Model):
    productgroup_id=models.ForeignKey(ProductGroup,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=200)
    description=models.CharField("description", max_length=200)
    price=models.FloatField("price",default=0)
    unit=models.CharField("unit", max_length=20)
    warranty=models.CharField("warranty", max_length=200)
    active=models.BooleanField("active",default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)

