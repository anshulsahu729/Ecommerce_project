from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from store.models import Product
from orders.models import Order
from accounts.models import User

User = get_user_model()

# Only allow staff or superusers to access
def staff_required(view_func):
    decorated_view_func = user_passes_test(
        lambda u: u.is_active and u.is_staff
    )(view_func)
    return decorated_view_func


# @staff_required
def dashboard(request):
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()
    recent_orders = Order.objects.order_by('-created_at')[:5]


    context = {
        'total_users': total_users,
        'total_orders': total_orders,
        'total_products': total_products,
        'recent_orders': recent_orders,
        
       
    }
    return render(request, 'adminpanel/dashboard.html', context)


# @staff_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

# @staff_required
def order_list(request):
    orders = Order.objects.all().select_related("user")
    return render(request, "orders/order_list.html", {"orders": orders})


# @staff_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})
