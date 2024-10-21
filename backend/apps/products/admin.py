from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from singlemodeladmin import SingleModelAdmin
from .models import Product, ProductType, ProductProperty, DeliveryPaymentDescription


class ProductPropertyInline(TranslationTabularInline):
    model = ProductProperty


@admin.register(ProductType)
class ProductTypeAdmin(TranslationAdmin):
    """Класс для описания интерфейса администрирования продуктов."""
    list_display = ('title', 'weight', 'is_enabled', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_editable = ('is_enabled', 'weight')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    """Класс для описания интерфейса администрирования продуктов."""
    list_display = ('title', 'is_enabled', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_editable = ('is_enabled',)
    list_filter = ('types',)
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ['related_products']
    inlines = [
        ProductPropertyInline,
    ]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "title",
                    "slug",
                    "short_description",
                    "short_description_2",
                    "long_description",
                    "image",
                    "types",
                    "price_unknown",
                    "price_description",
                    "is_enabled",
                    "related_products",
                ],
            },
        ),
        (
            "SEO",
            {
                "classes": ["collapse"],
                "fields": [
                    "meta_h1",
                    "meta_title",
                    "meta_keywords",
                    "meta_description",
                ],
            },
        ),
    ]


@admin.register(DeliveryPaymentDescription)
class DeliveryPaymentDescriptionAdmin(SingleModelAdmin, TranslationAdmin):
    pass
