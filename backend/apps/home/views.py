from django.views.generic.base import TemplateView
from .models import ProductType, Product, ContactData, PageData
from django.views.generic.edit import FormView
from .forms import OrderForm


class HomeView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['product_types'] = ProductType.objects.enabled()
        context['products'] = Product.objects.enabled()
        context['contact_data'] = ContactData.objects.first()
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
