from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Category, Product
from .forms import ProductForm

class AddProductView(CreateView):
    model=Product
    form_class = ProductForm
    template_name = "products/add_product.html"

