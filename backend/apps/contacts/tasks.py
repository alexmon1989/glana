from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from backend.celery import app


@app.task
def send_email(data):
    # Отправка E-Mail
    subject = '{} Повідомлення клієнта з сайту'.format(settings.EMAIL_SUBJECT_PREFIX)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [a[1] for a in settings.MANAGERS]
    html_content = render_to_string('contacts/email.html', data)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
