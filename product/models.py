from __future__ import unicode_literals
from django.db import models
import django.utils.safestring as safestring
from django.conf import settings


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
    image=models.ImageField(upload_to='uploads/%Y/%m/%d/',default='')

    def image_tag(self):    
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

