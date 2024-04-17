from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import translator, TranslationOptions
from .models import Product, ProductType, ContactData, PageData


class PageDataOptions(TranslationOptions):
    fields = ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description')


class ProductTypeOptions(TranslationOptions):
    fields = ('title', )


class ProductOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


translator.register(PageData, PageDataOptions)
translator.register(ProductType, ProductTypeOptions)
translator.register(Product, ProductOptions)


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
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactData)
class ContactDataAdmin(SingleModelAdmin):
    """Класс для описания интерфейса администрирования контактных данных."""
    pass


@admin.register(PageData)
class PageDataAdmin(SingleModelAdmin, TranslationAdmin):
    """Класс для описания интерфейса администрирования данных страницы."""
    pass
