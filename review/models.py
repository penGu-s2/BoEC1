from django.db import models
from django.utils.translation import activate
from boec.models import User
from item.models import Item
# Create your models here.
class review(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    rating=models.FloatField("rating",default=1)
    content=models.CharField("content",max_length=200)
    active=models.BooleanField("active",default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)