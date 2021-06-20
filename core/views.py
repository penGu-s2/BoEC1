from django.http import request
from django.shortcuts import render
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'homepages/homepage.html')

class CheckoutView(View):
    def get(self,request):
        return render(request,'checkout/checkoutpage.html')
class ProductView(View):
    def get(self,request):
        return render(request,'product/productpage.html')