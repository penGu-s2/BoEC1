from django.db import models
from django.conf import settings
from order.models import Cart
import django.utils.safestring as safestring
from product.models import Product
from django.utils.safestring import mark_safe
# Create your models here.


class Item(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name=models.CharField("name",max_length=200)
    color = models.CharField("color", max_length=200)
    size = models.CharField("size", max_length=200)
    sellPrice= models.FloatField("sellPrice",default=0)
    salePrice= models.FloatField("salePrice",default=0)    
    quantity = models.IntegerField("quantity", default=0)
    active=models.BooleanField("active",default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
    
    def color_tag(self):
        if self.color is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.color))
        else:
            return ""
class CartItem(models.Model):
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    quantity=models.IntegerField("quantity",default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)

class ItemImage(models.Model):
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='uploads/%Y/%m/%d/')
    def image_tag(self):    
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True