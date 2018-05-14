from django import forms
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class OrderForm(forms.Form):
    """Класс формы просчёта заказа."""
    username = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(max_length=1024)
    file = forms.FileField(max_length=5242880, required=False)

    def send_email(self):
        # Отправка E-Mail
        subject = '{} Сообщение клиента с сайта'.format(settings.EMAIL_SUBJECT_PREFIX)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = [a[1] for a in settings.MANAGERS]
        html_content = render_to_string('home/email_order.html', self.cleaned_data)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        if self.cleaned_data['file']:
            msg.attach(
                self.cleaned_data['file'].name,
                self.cleaned_data['file'].read(),
                self.cleaned_data['file'].content_type
            )
        msg.send()
