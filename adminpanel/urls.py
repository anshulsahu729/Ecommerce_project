from django.urls import path
from . import views

app_name = "adminpanel"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('orders/', views.order_list, name='order_list'),
    path('products/', views.product_list, name='product_list'),
]
