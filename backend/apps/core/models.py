from django.db import models
from django.core.cache import cache


class SeoModel(models.Model):
    """Модель для SEO-тегов."""
    meta_h1 = models.CharField('H1', blank=True, max_length=255)
    meta_title = models.CharField('Title', blank=True, max_length=255)
    meta_description = models.TextField('Description', blank=True, max_length=255)
    meta_keywords = models.TextField('Keywords', blank=True, max_length=255)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """Абстрактный класс модели, содержащий описания полей created_at, updated_at."""
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        abstract = True


class CacheClearModel(models.Model):
    """Базовая модель, очищающая кеш при сохранении."""
    def save(self, *args, **kwargs):
        cache.clear()
        return super(CacheClearModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
