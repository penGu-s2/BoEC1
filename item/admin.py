from __future__ import unicode_literals
from django.contrib import admin
from .models import Item,CartItem,ItemImage
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    readonly_fields = ('salePrice',)    
    list_display = ('name', 'color','size','sellPrice'
                    ,'salePrice','quantity','active','create_at','dateUpdate','color_tag')
class CartItemAdmin(admin.ModelAdmin):
    readonly_fields = ('cart_id','item_id','id',)    
    list_display = ('quantity','item_id','cart_id','create_at','dateUpdate')
class ItemImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)    

admin.site.register(Item,ItemAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(ItemImage,ItemImageAdmin)
     