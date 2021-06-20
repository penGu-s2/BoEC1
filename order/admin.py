from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Cart,Order,Shipment,Payment
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'id', 'isUsing', 'create_at', 'dateUpdate']
    list_filter = ['isUsing', ]
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'ward', 'district', 'city', 'status']
    list_filter = ['status']
    readonly_fields = ('cart_id', 'name', 'recipientName',
                       'create_at', 'dateUpdate', 'status')
    search_fields = ('name',)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'type','price', 'create_at']
    list_filter = ['type']
    readonly_fields = ('type', 'price','dateUpdate', 'create_at', 'id')
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['paymentMethod', 'paid','prePayment', 'create_at']
    list_filter = ['paymentMethod']

admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Shipment,ShipmentAdmin)
admin.site.register(Payment,PaymentAdmin)
    