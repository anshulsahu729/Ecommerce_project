from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Order
from .forms import CategoryForm, ProductForm, OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from blog.models import BlogPost
from newsletter.forms import NewsletterSignupForm



def home(request):
    # Featured products
    products = Product.objects.filter(active=True)[:6]

    # Latest blogs with pagination
    blog_list = BlogPost.objects.all().order_by('-published_date')
    paginator = Paginator(blog_list, 3)  # 3 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Newsletter form
    form = NewsletterSignupForm()

    return render(request, "store/home.html", {
    "products": products,
    "blog_list": blog_list,
    "page_obj": page_obj,
    "form": form,
})

    




# -------------------- CATEGORY --------------------

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            return redirect('store:category_list')  # Make sure this URL name exists
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CategoryForm()
    
    return render(request, 'store/category_form.html', {'form': form, 'title': 'Create Category'})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('store:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'store/category_form.html', {'form': form, 'title': 'Edit Category'})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('store:category_list')
    return render(request, 'store/category_confirm_delete.html', {'category': category})

# -------------------- PRODUCT --------------------

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})

@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("store:product_list")
    else:
        form = ProductForm()
    return render(request, "store/product_form.html", {"form": form, 'title': 'Add Product'})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('store:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form, 'title': 'Edit Product'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('store:product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

# -------------------- ORDER --------------------

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'store/order_list.html', {'orders': orders})

@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:order_list')
    else:
        form = OrderForm()
    return render(request, 'store/order_form.html', {'form': form, 'title': 'Add Order'})

@login_required
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('store:order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'store/order_form.html', {'form': form, 'title': 'Edit Order'})

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('store:order_list')
    return render(request, 'store/order_confirm_delete.html', {'order': order})
