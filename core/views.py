from django.shortcuts import render, get_object_or_404
from store.models import Product, Category
from blog.models import BlogPost


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
def product_list(request):
    categories = Category.objects.all()[:4]  

    category_products = {}
    for category in categories:
        category_products[category] = Product.objects.filter(
            category=category, active=True
        )[:4]

    return render(request, "core/home.html", {
        "category_products": category_products,
    })

def blog_list(request):
    blogs = BlogPost.objects.filter(active=True,deleted=False).order_by("-published_date") 
    return render(request, "core/blog.html", {"blogs": blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug, active=True, deleted=False)
    return render(request, "core/blog_detail.html", {"blog": blog})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, active=True)

    return render(request, "core/category_products.html", {
        "category": category,
        "products": products,
    })
