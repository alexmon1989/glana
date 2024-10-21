from django.db.models import Prefetch

from .models import ProductType, Product


def product_type_get_list_with_products() -> list:
    """Возвращает список типаов продуктов с продуктами."""
    product_types = ProductType.objects.enabled().order_by(
        '-weight'
    ).prefetch_related(
        Prefetch('product_set', queryset=Product.objects.filter(is_enabled=True))
    )
    res = []

    for product_type in product_types:
        item = {'title': product_type.title, 'products': []}
        for product in product_type.product_set.all():
            item['products'].append(product)
        res.append(item)

    return res
