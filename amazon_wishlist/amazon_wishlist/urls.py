from django.contrib import admin
from django.urls import path, include  # Include 'include'

from wishlist import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('top-price-changes/', views.top_price_changes_view, name='top_price_changes'),
    path('categories/', views.categories_view, name='categories'),
    path('search/', views.search_view, name='search'),
    path('wishlist/', include('wishlist.urls')),  # This includes 'wishlist/urls.py'
]
