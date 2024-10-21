from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import ProductManager, ProductTypeManager
from .utils import get_products_upload_to_folder

from apps.core.models import TimeStampedModel, CacheClearModel, SeoModel


class ProductType(SeoModel, TimeStampedModel, CacheClearModel):
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


class Product(SeoModel, TimeStampedModel, CacheClearModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Slug', null=True)
    short_description = models.CharField('Краткое описание (главная страница)', max_length=255)
    short_description_2 = RichTextUploadingField(
        'Краткое описание (страница товара)',
        blank=True,
        null=True
    )
    long_description = RichTextUploadingField('Длинное описание', blank=True, null=True)
    image = ThumbnailerImageField(
        verbose_name='Изображение',
        upload_to=get_products_upload_to_folder,
        blank=True
    )
    price_unknown = models.BooleanField('Стоимость неизвестна', default=False)
    price_description = RichTextUploadingField(
        'Стоимость',
        blank=True,
        null=True,
        help_text='Не будет отображаться на странице товара если включено поле "Стоимость неизвестна".'
    )
    is_enabled = models.BooleanField('Включено', default=True)
    types = models.ManyToManyField(ProductType, verbose_name='Тип продукта')
    related_products = models.ManyToManyField('self', symmetrical=False, verbose_name='Связанные продукты')

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_types_string(self):
        return ' '.join([x.slug for x in self.types.all()])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
        ordering = ('title',)


class ProductProperty(TimeStampedModel):
    """Модель характеристики продукта."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField('Название', max_length=255)
    value = models.CharField('Значение', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Характеристика продукта'
        verbose_name_plural = 'Характеристики продукта'


class DeliveryPaymentDescription(TimeStampedModel):
    """Модель блока описания доставки и оплаты."""
    block_title = models.CharField('Название блока', max_length=255)
    content = RichTextUploadingField('Содержание')

    def __str__(self):
        return self.block_title

    class Meta:
        verbose_name = 'Оплата и доставка'
        verbose_name_plural = 'Оплата и доставка'
