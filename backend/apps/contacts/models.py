from django.db import models
from backend.abstract_models import CacheClearModel


class ContactData(CacheClearModel):
    """Модель контактных данных"""
    contact_email = models.EmailField('E-Mail для контактов')
    form_email = models.EmailField('E-Mail для форм', max_length=255)
    phone = models.CharField('Телефон', max_length=255)
    operator = models.SmallIntegerField('Оператор', choices=((1, 'Киевстар'),), default=1, null=True, blank=True)
    fb_link = models.URLField('Ссылка Facebook', null=True, blank=True)
    instagram_link = models.URLField('Ссылка Instagram', null=True, blank=True)

    def __str__(self):
        return 'Контактные данные'

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'
