from django.shortcuts import render

from .models import DeliveryPage


def index(request):
    """Отображает страницу."""
    page, created = DeliveryPage.objects.get_or_create()
    return render(request, 'delivery/index/index.html', {'page': page})
