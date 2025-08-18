from django.shortcuts import render, redirect, get_object_or_404
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from store.models import Product
@login_required(login_url='accounts:login')
def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        return redirect("cart:cart_detail")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user   
            order.save()

            for product_id, qty in cart.items():
                product = get_object_or_404(Product, id=product_id)
                OrderItem.objects.create(
                    order=order, product=product, quantity=qty, price=product.price
                )

            # clear cart
            request.session["cart"] = {}

            return redirect("orders:thankyou")
    else:
        form = CheckoutForm()

    return render(request, "orders/checkout.html", {"form": form})


def thankyou(request):
    
    return render(request, "orders/thankyou.html")
