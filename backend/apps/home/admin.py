from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import PageData


@admin.register(PageData)
class PageDataAdmin(SingleModelAdmin, TranslationAdmin):
    """Класс для описания интерфейса администрирования данных страницы."""
    pass
