import random
import string

from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField
from backend.abstract_models import TimeStampedModel, CacheClearModel, SeoModel


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
        return super(ProductManager, self).get_queryset().prefetch_related('types').filter(is_enabled=True)


def upload_to(instance, filename):
    return '/'.join(['products', ''.join(random.choices(string.ascii_uppercase + string.digits, k=2)), filename])


class Product(TimeStampedModel, CacheClearModel):
    """Модель продукта."""
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Slug', null=True)
    short_description = models.CharField('Краткое описание', max_length=255)
    long_description = RichTextUploadingField('Длинное описание', blank=True, null=True)
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
        return ' '.join([x.slug for x in self.types.all()])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'
        ordering = ('title',)


class ContactData(CacheClearModel):
    """Модель контактных данных"""
    contact_email = models.EmailField('E-Mail для контактов')
    form_email = models.EmailField('E-Mail для форм', max_length=255)
    phone = models.CharField('Телефон', max_length=255)
    operator = models.SmallIntegerField('Оператор', choices=((1, 'Киевстар'),), default=1, null=True, blank=True)
    fb_link = models.URLField('Ссылка Facebook', null=True, blank=True)
    instagram_link = models.URLField('Ссылка Instagram', null=True, blank=True)
    twitter_link = models.URLField('Ссылка Twitter', null=True, blank=True)

    def __str__(self):
        return 'Контактные данные'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'


class PageData(SeoModel, TimeStampedModel):
    """Модель данных страницы (метаданные и т.д.)."""
    ga_html = models.TextField('HTML-код Google Analytics', default=None, null=True, blank=True)

    def __str__(self):
        return 'Данные страницы'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
