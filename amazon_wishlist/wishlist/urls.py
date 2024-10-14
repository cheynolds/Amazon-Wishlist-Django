from django.urls import path
from . import views

urlpatterns = [
	path('products/', views.products_view, name='products'),  # Ensure 'products' is the correct name
	path('products/<str:asin>/', views.product_detail_view, name='product_detail'),
	path('wishlist/<str:wishlist_name>/', views.wishlist_products, name='wishlist_products'),
	
]
