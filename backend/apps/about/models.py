from ckeditor_uploader.fields import RichTextUploadingField

from apps.core.models import SeoModel


class AboutPage(SeoModel):
    """Модель страницы доставки."""
    content = RichTextUploadingField(verbose_name='Содержание', blank=True)

    def __str__(self):
        return 'Страница "О нас"'

    class Meta:
        verbose_name = 'Страница "О нас"'
        verbose_name_plural = 'Страница "О нас"'
