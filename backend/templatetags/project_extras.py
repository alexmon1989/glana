from django import template
from django.urls import translate_url

from apps.contacts.models import ContactData
from apps.contacts.services import contacts_get_data
from apps.products.services import product_type_get_list_with_products


register = template.Library()


@register.simple_tag(takes_context=True)
def change_language(context, lang=None, *args, **kwargs) -> str:
    path = context['request'].get_full_path()
    return translate_url(path, lang)


@register.simple_tag
def product_types() -> list:
    return product_type_get_list_with_products()


@register.simple_tag
def contact_data() -> ContactData:
    return contacts_get_data()
