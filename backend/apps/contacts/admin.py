from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import ContactData


@admin.register(ContactData)
class ContactDataAdmin(SingleModelAdmin):
    """Класс для описания интерфейса администрирования контактных данных."""
    pass
