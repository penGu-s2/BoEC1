from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  
   path('', views.homepage  , name = "homepage"),
   path('productdetail/<int:product_id>/', views.productdetail  , name = "productdetail"),
   path('cart/' ,views.cart , name = "cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)