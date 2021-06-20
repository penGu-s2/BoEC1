from __future__ import unicode_literals
from django.contrib import admin
from .models import Account,Fullname,User,Address
# Register your models here.


class AccountAdmin(admin.ModelAdmin):  
    list_display = ('usernames','passwords')
class FullnameAdmin(admin.ModelAdmin): 
    list_display = ('firstName','middleName','lastName','create_at','dateUpdate')    
class UserAdmin(admin.ModelAdmin):
    list_filter=('active',)
    readonly_fields = ('fullname_id','account_id','id',)    
    list_display = ('idCard', 'dob','gender','phoneNumber'
                    ,'coin','facebookID','active','facebookName','googleEmail','googleName')
class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('user_id',)    
    list_display = ('detailedAddress','city','country','create_at','dateUpdate')   
admin.site.register(Account,AccountAdmin)
admin.site.register(Fullname,FullnameAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Address,AddressAdmin)
