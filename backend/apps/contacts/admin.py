from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from singlemodeladmin import SingleModelAdmin
from .models import ContactData


@admin.register(ContactData)
class ContactDataAdmin(TranslationAdmin, SingleModelAdmin):
    """Класс для описания интерфейса администрирования контактных данных."""
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "address",
                    "contact_email",
                    "form_email",
                    "phone",
                    "operator",
                    "fb_link",
                    "instagram_link",
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
