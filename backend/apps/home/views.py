from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from .models import PageData
from .forms import OrderForm
from apps.products.models import ProductType, Product
from apps.contacts.services import contacts_get_data


class HomeView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['product_types'] = ProductType.objects.enabled()
        context['products'] = Product.objects.enabled()
        context['contact_data'] = contacts_get_data()
        context['page_data'] = PageData.objects.first()

        return context


class OrderView(FormView):
    """Отправляет данные о просчёте заказа."""
    http_method_names = ('post',)
    form_class = OrderForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ProductDescriptionDetailView(DetailView):
    """Отображает данные описания товара."""
    template_name = 'home/product_description.html'
    model = Product
