from __future__ import unicode_literals
from django.db.models.fields import DateField

from django.http import Http404
from django.shortcuts import render, redirect
from .models import ProductGroup,Catalog, Product
# Create your views here.

def homepage(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    store_items = Product.objects.all()
    ctx={
        'store_items':store_items,
    }
    return render(request , "homepages/homepage.html" , ctx)


def productdetail(request,product_id):
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    request.session.set_expiry(0)
    try:
        store_items1 = Product.objects.all()
        product = Product.objects.get(id=product_id)
        ctx={
             'store_items1':store_items1,
             'product': product,
             'cart_size' : len(cart),
            
        }
       
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    if request.method == "POST":
        cart.append(int(request.POST['obj_id']))
        return  redirect('productdetail')
        
    return render(request, 'product/productpage.html', ctx)
def cartItems(cart):
    items = []
    #the products that are added to cart , now will be gotten from DB
    #and they will be added in items
    for item in cart:
        #we added products by their id , so item here is the id
        #and we use this item to be = id in query
        items.append(Product.objects.get(id=item))
    return items
def priceCart(cart):
    cart_items = cartItems(cart)
    price = 0
    for item in cart_items:
        price += item.price
    return price
def cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {
        'cart':cart ,
        #the number of products in cart
        'cart_size' : len(cart) ,
        #the porduct in cart
        'cart_items': cartItems(cart),
        #the total price of each product in cart by knwoing its number
        'total_price':priceCart(cart),
    }
    return render(request , 'product/cart.html' , ctx)