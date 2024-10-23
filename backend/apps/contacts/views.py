from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


from .models import ContactData
from .forms import ContactsForm


class ContactFormView(SuccessMessageMixin, FormView):
    template_name = 'contacts/index/index.html'
    form_class = ContactsForm
    success_url = reverse_lazy("contacts:index")
    success_message = _('Повідомлення успішно відправлено.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_data, created = ContactData.objects.get_or_create()
        context['contact_data'] = contact_data
        return context

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
