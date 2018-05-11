from django.views.generic.base import TemplateView
from .models import ProductType, Product, ContactData


class HomeView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['product_types'] = ProductType.objects.enabled()
        context['products'] = Product.objects.enabled()
        context['contact_data'] = ContactData.objects.first()

        return context
