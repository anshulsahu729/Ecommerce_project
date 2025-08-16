from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


# List blogs with pagination
def blog_list(request):
    posts = BlogPost.objects.filter(active=True, deleted=False).order_by("-published_date")
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/blog_list.html", {"page_obj": page_obj})


# Blog detail view
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "blog/blog_detail.html", {"post": post})



# Create a new blog post
@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = slugify(blog.title)
            blog.save()
            messages.success(request, "Blog post created successfully.")
            return redirect("blog:blog_detail", slug=blog.slug)
 
    else:
        form = BlogPostForm()
    return render(request, "blog/blog_form.html", {"form": form})



# Update an existing blog post
@login_required
def blog_update(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk, deleted=False)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully.")
            return redirect("blog:blog_detail", slug=blog.slug)
    else:
        form = BlogPostForm(instance=blog)
    return render(request, "blog/blog_form.html", {"form": form})


# Soft delete a blog post
@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk, deleted=False)
    blog.deleted = True
    blog.save()
    messages.warning(request, "Blog post deleted (soft delete).")
    return redirect("blog:blog_list")

