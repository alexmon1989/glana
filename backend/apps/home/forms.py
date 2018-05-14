from django import forms
from .tasks import send_email


class OrderForm(forms.Form):
    """Класс формы просчёта заказа."""
    username = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(max_length=1024)
    file = forms.FileField(max_length=5242880, required=False)

    def send_email(self):
        # Асинхронная отправка E-Mail
        data = self.cleaned_data.copy()
        if data['file']:
            data['file'] = {
                'name': self.cleaned_data['file'].name,
                'read': self.cleaned_data['file'].read(),
                'content_type': self.cleaned_data['file'].content_type,
            }
        send_email.delay(data)
