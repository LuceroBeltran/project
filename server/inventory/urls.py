from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexApi.as_view(), name='index'),

    path('products/', views.ProductoView.as_view(), name='productos'),  
    path('products/<int:product_id>/', views.ProductoView.as_view(), name='producto_detail'),  

    path('nfc/', views.NFCView.as_view(), name='nfc'), 
    path('nfc/<int:nfc_id>/', views.NFCView.as_view(), name='nfc_detail'),  

    path('categories/', views.CategoryView.as_view(), name='categories'), 
    path('categories/<int:category_id>/', views.CategoryView.as_view(), name='category_detail'),
]
