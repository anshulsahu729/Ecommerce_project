from django import forms
from .models import Category, Product, Order

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
            'slug': forms.TextInput(attrs={'placeholder': 'Enter slug'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'description', 'stock', 'image', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Enter stock quantity'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter product description', 'rows': 3}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'phone', 'total_price', 'status']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter your address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'total_price': forms.NumberInput(attrs={'placeholder': 'Enter total price'}),
            'status': forms.Select(choices=Order.STATUS_CHOICES),
        }
