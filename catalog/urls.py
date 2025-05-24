# catalog/urls.py

from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('products/<int:pk>/unpublish/', views.product_unpublish, name='product_unpublish'),
    path('category/<int:category_id>/', views.products_by_category, name='product_by_category'),
]
