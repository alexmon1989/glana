from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django_recaptcha.widgets import ReCaptchaV3


class CustomReCaptchaV3(ReCaptchaV3):
    """
    Виджет ReCaptchaV3 с переопределённым шаблоном из папки проекта.
    Рендерится напрямую через render_to_string, минуя форм-рендерер,
    что позволяет использовать шаблон из DIRS без FORM_RENDERER = TemplatesSetting.
    """

    custom_template = 'django_recaptcha/widget_v3.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        return mark_safe(render_to_string(self.custom_template, context))
