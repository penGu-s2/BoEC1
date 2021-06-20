from django.contrib.auth.models import User
from django.db import models

from boec.models import User

# Create your models here.
class Cart(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    isUsing=models.BooleanField("isUsing",default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
class Order(models.Model):
    STATUS = (
        ('ToPay', 'ToPay'),
        ('ToShip', 'ToShip'),
        ('ToReceive', 'ToReceive'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('ReturnRefund', 'ReturnRefund'),
    )
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=200)
    recipientName = models.CharField("recipientName", max_length=200)
    recipientPhoneNumber = models.CharField("recipientPhoneNumber", max_length=200)
    recipientEmail = models.CharField("recipientEmail", max_length=200)
    detailedAddress = models.CharField("detailedAddress", max_length=200)
    ward = models.CharField("ward", max_length=200)
    district = models.CharField("district", max_length=200)
    city = models.CharField("city", max_length=200)
    country = models.CharField("country", max_length=200)
    note = models.CharField("note", max_length=200)
    status = models.CharField(max_length=10, choices=STATUS, default='ToPay')
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
    def __str__(self):
        return self.name
class Shipment(models.Model):
    ShipmentCompany=(
        ('VNPost','VNPost'),
        ('GiaoHangTietKiem','GiaoHangTietKiem'),
        ('Now', 'Now'),
        ('Grab', 'Grab'),
    )
    id = models.AutoField(primary_key=True)
    company=models.CharField(max_length=20, choices=ShipmentCompany, default='VNPost')
    ShipmentType =(
        ('Express','Express'),
        ('Fast','Fast'),
        ('Ordinary', 'Ordinary'),
        ('Free', 'Free'),
    )
    type=models.CharField(max_length=20, choices=ShipmentType, default='Express')
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
class Payment(models.Model):
    STATUS=(
        ('OnDelivery','OnDelivery'),
        ('MOMO','MOMO'),
        ('VNPAY', 'VNPAY'),
        ('ZaloPay', 'ZaloPay'),
        ('VisaCard', 'VisaCard'),
        ('CreditCard', 'CreditCard'),
        ('BankCard', 'BankCard'),
    )
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE)
    shipment_id=models.ForeignKey(Shipment,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    paymentMethod = models.CharField(max_length=10, choices=STATUS, default='OnDelivery')
    paid=models.BooleanField("paid",default=False)
    prePayment = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
    def __str__(self):
        return self.paid

