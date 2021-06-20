from django.db import models

# Create your models here.

#User
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    usernames = models.CharField("Username", max_length=200)
    passwords=models.CharField("Password", max_length=200)
class Fullname(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField("firstName", max_length=200)
    middleName=models.CharField("middleName", max_length=200)
    lastName=models.CharField("lastName", max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
class User(models.Model):
    fullname_id=models.ForeignKey(Fullname,on_delete=models.CASCADE)
    account_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    idCard = models.CharField("idCard", max_length=50)
    dob = models.DateTimeField("dob",auto_now_add=True, blank=True)
    gender = models.CharField("gender", max_length=50)
    phoneNumber=models.CharField("phoneNumber", max_length=200)
    coin=models.IntegerField("coin", default=0)
    facebookID=models.CharField("facebookID", max_length=200)
    facebookName=models.CharField("facebookName", max_length=200)
    googleEmail=models.CharField("googleEmail", max_length=200)
    googleName=models.CharField("googleName", max_length=200)
    active=models.BooleanField("active",default=False)
    
    def __str__(self):
        return self.account_id.usernames
class Address(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    detailedAddress = models.CharField("detailedAddress", max_length=200)
    city=models.CharField("city", max_length=200)
    country=models.CharField("country", max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField("dateUpdate",auto_now_add=True, blank=True)
