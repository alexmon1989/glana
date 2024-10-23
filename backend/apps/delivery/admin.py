from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from singlemodeladmin import SingleModelAdmin

from .models import DeliveryPage


@admin.register(DeliveryPage)
class ContactDataAdmin(TranslationAdmin, SingleModelAdmin):
    """Класс для описания интерфейса администрирования страницы доставки."""
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "content",
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
