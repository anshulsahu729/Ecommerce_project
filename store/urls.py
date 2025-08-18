from django.urls import path
from . import views

app_name = 'store'  
urlpatterns = [
    
    # ---------------- Category URLs ----------------
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # ---------------- Product URLs ----------------
    path("products/", views.product_list, name="product_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("products/create/", views.product_create, name="product_create"),
    path('products/<int:pk>/edit/', views.product_update, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # ---------------- Order URLs ----------------
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_create, name='order_add'),
    path('orders/<int:pk>/edit/', views.order_update, name='order_edit'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
]
