from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Column

from .tasks import send_email


class ContactsForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, label='ПІБ')
    email = forms.EmailField(max_length=255, label='E-Mail')
    subject = forms.CharField(max_length=255, required=False, label='Тема повідомлення')
    phone = forms.CharField(max_length=255, required=False, label='Ваш телефон')
    message = forms.CharField(min_length=10, max_length=1024, label='Текст повідомлення', widget=forms.Textarea)

    def send_email(self):
        # Асинхронная отправка E-Mail
        send_email.delay(self.cleaned_data)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contacts-form'
        self.helper.form_method = 'post'

        self.fields['username'].widget.attrs.update({
            'class': 'form-control g-py-13 g-px-15',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control g-py-13 g-px-15',
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control g-py-13 g-px-15',
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control g-py-13 g-px-15',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control g-resize-none rounded-3 g-py-13 g-px-15',
            'rows': 7,
        })

        # self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='col-12 col-lg-6'),
                Column('email', css_class='col-12 col-lg-6'),
            ),
            Row(
                Column('subject', css_class='col-12 col-lg-6'),
                Column('phone', css_class='col-12 col-lg-6'),
            ),
            Row(
                Column('message', css_class='col-md-12 g-mb-20'),
            ),
            Div(template='contacts/index/_partials/submit.html')
        )
