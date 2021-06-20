from django.contrib import admin

from .models import Catalog,ProductGroup,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('create_at',)
    list_display = ('id','name', 'create_at','dateUpdate', )
    
class ProdcutGroupAdmin(admin.ModelAdmin):
    list_filter = ('create_at',)
    list_display = ('id','name', 'create_at','dateUpdate', )

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('id','name','description','price','unit','warranty','active', 'create_at','dateUpdate', )

admin.site.register(Catalog, CategoryAdmin)
admin.site.register(ProductGroup, ProdcutGroupAdmin)
admin.site.register(Product, ProductAdmin)