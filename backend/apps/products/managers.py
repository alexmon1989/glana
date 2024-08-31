from django.db import models


class ProductTypeManager(models.Manager):
    def enabled(self):
        """Возвращает типы продуктов с is_enabled=True."""
        return super(ProductTypeManager, self).get_queryset().filter(is_enabled=True)
    

class ProductManager(models.Manager):
    def enabled(self):
        """Возвращает продукты с is_enabled=True."""
        return super(ProductManager, self).get_queryset().prefetch_related('types').filter(is_enabled=True)
