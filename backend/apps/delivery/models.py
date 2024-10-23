from ckeditor_uploader.fields import RichTextUploadingField

from apps.core.models import SeoModel


class DeliveryPage(SeoModel):
    """Модель страницы доставки."""
    content = RichTextUploadingField(verbose_name='Содержание', blank=True)

    def __str__(self):
        return 'Страница "Доставка"'

    class Meta:
        verbose_name = 'Страница "Доставка"'
        verbose_name_plural = 'Страница "Доставка"'
