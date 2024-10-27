from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from apps.products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    related_products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.filter(is_enabled=True),
        required=False,
        widget=FilteredSelectMultiple("Связанные продукты", is_stacked=False),
    )
