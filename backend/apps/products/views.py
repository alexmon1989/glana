from django.views.generic.detail import DetailView

from .models import Product, DeliveryPaymentDescription


class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.enabled().prefetch_related('productproperty_set', 'related_products')
    template_name = 'products/detail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivery_desc'] = DeliveryPaymentDescription.objects.first()
        return context
