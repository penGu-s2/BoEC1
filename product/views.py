from __future__ import unicode_literals
from django.db.models.fields import DateField

from django.http import Http404
from django.shortcuts import render
from .models import ProductGroup,Catalog, Product
# Create your views here.

def homepage(request):
    store_items = Product.objects.all()
    ctx={
        'store_items':store_items,
    }
    return render(request , "homepages/homepage.html" , ctx)
def productdetail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product/productpage.html', {'product': product})