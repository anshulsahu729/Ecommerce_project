from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import SignupForm, LoginForm
from orders.models import Order
from store.models import Product

def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('accounts:login')  # ✅ Use namespace
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    error = None

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user, backend='accounts.backends.SHAAuthBackend')
                return redirect('accounts:dashboard')  # ✅ Use namespace
            else:
                error = "Invalid password"
        except User.DoesNotExist:
            error = "User not found"

    return render(request, 'accounts/login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # ✅ Use namespace

@login_required
def dashboard_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]
    saved_items = Product.objects.filter(is_featured=True)[:3]

    total_orders = orders.count()
    cart_items_count = sum(request.session.get('cart', {}).values())

  


    context = {
        'orders': orders,
        'saved_items': saved_items,
        'total_orders': total_orders,
        'cart_items_count': cart_items_count,
        
        # You can add wishlist_count or saved_items_count if you implement those models
    }
 
    return render(request, 'accounts/dashboard.html', context)
