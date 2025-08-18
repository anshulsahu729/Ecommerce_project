from django.urls import path
from . import views
app_name = "core"
urlpatterns = [
    path("home/", views.home, name="home"),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
    path("products/", views.product_list, name="product_list"),
    path("blogs/", views.blog_list, name="blog_list"),
    path("blogs/<slug:slug>/detail/", views.blog_detail, name="blog_detail"),
]
