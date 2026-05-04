from django.shortcuts import render

from .models import AboutPage
from apps.home.forms import OrderForm


def index(request):
    """Отображает страницу."""
    page, created = AboutPage.objects.get_or_create()
    return render(request, 'about/index/index.html', {'page': page, 'order_form': OrderForm()})
