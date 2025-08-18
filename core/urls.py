from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
]
