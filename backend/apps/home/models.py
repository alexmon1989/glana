import random
import string

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from backend.abstract_models import TimeStampedModel, CacheClearModel


class ProductTypeManager(models.Manager):
    def enabled(self):
        """Возвращает типы продуктов с is_enabled=True."""
        return super(ProductTypeManager, self).get_queryset().filter(is_enabled=True)


class ProductType(TimeStampedModel, CacheClearModel):
    """Модель типа продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Slug (для url)',
        max_length=255,
        default=''
    )
    weight = models.IntegerField(
        'Вес',
        default=1000,
        help_text='Чем больше вес, тем выше на странице находится этот тип продукта.'
    )
    is_enabled = models.BooleanField('Включено', default=True)

    objects = ProductTypeManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'
        ordering = ('-weight',)


class ProductManager(models.Manager):
    def enabled(self):
        """Возвращает продукты с is_enabled=True."""
        return super(ProductManager, self).get_queryset().filter(is_enabled=True)


def upload_to(instance, filename):
    return '/'.join(['products', ''.join(random.choices(string.ascii_uppercase + string.digits, k=2)), filename])


class Product(TimeStampedModel, CacheClearModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    short_description = models.CharField('Краткое описание', max_length=255)
    image = ThumbnailerImageField(
        verbose_name='Изображение',
        upload_to=upload_to,
        blank=True
    )
    is_enabled = models.BooleanField('Включено', default=True)
    types = models.ManyToManyField(ProductType, verbose_name='Тип продукта')

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_types_string(self):
        return ' '.join(self.types.values_list('slug')[0])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
        ordering = ('title',)
