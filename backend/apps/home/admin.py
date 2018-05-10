from django.contrib import admin
from .models import Product, ProductType


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования продуктов."""
    list_display = ('title', 'weight', 'is_enabled', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_editable = ('is_enabled', 'weight')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования продуктов."""
    list_display = ('title', 'is_enabled', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_editable = ('is_enabled',)
    list_filter = ('types',)
