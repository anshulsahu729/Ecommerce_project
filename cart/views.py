from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product

def cart_detail(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * qty
        total += subtotal
        cart_items.append({"product": product, "qty": qty, "subtotal": subtotal})

    return render(request, "cart/cart_detail.html", {"cart_items": cart_items, "total": total})


def cart_add(request, product_id):
    cart = request.session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session["cart"] = cart
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session["cart"] = cart
    return redirect("cart:cart_detail")


def cart_clear(request):
    request.session["cart"] = {}
    return redirect("cart:cart_detail")
