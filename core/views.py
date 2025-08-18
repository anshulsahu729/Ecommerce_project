from django.shortcuts import render, get_object_or_404
from store.models import Product, Category


def home(request):
    categories = Category.objects.all()[:4]  

    category_products = {}
    for category in categories:
        category_products[category] = Product.objects.filter(
            category=category, active=True
        )[:4]

    return render(request, "core/home.html", {
        "category_products": category_products,
    })


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, active=True)

    return render(request, "core/category_products.html", {
        "category": category,
        "products": products,
    })
