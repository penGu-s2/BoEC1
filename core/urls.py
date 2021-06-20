from django.urls import path
from .views import HomeView,CheckoutView,ProductView

urlpatterns = [
    path('', HomeView.as_view(),name='homepage'),
    path('checkout/', CheckoutView.as_view(),name='checkoutpage'),
    path('productdetail/', ProductView.as_view(),name='product'),
]
