from django.contrib import admin
from .models import Category, Product
# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass