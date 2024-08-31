from typing import Any
from django.db.models.query import QuerySet
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import Product


class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.enabled()
    template_name = 'products/detail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    