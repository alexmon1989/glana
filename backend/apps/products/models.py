from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import ProductManager, ProductTypeManager
from .utils import get_products_upload_to_folder

from backend.abstract_models import TimeStampedModel, CacheClearModel


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


class Product(TimeStampedModel, CacheClearModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Slug', null=True)
    short_description = models.CharField('Краткое описание', max_length=255)
    long_description = RichTextUploadingField('Длинное описание', blank=True, null=True)
    image = ThumbnailerImageField(
        verbose_name='Изображение',
        upload_to=get_products_upload_to_folder,
        blank=True
    )
    is_enabled = models.BooleanField('Включено', default=True)
    types = models.ManyToManyField(ProductType, verbose_name='Тип продукта')

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_types_string(self):
        return ' '.join([x.slug for x in self.types.all()])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
        ordering = ('title',)
