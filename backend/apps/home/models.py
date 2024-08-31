from django.db import models
from backend.abstract_models import TimeStampedModel, SeoModel


class PageData(SeoModel, TimeStampedModel):
    """Модель данных страницы (метаданные и т.д.)."""
    ga_html = models.TextField('HTML-код Google Analytics', default=None, null=True, blank=True)

    def __str__(self):
        return 'Данные страницы'

    class Meta:
        verbose_name = 'Данные страницы'
        verbose_name_plural = 'Данные страницы'
