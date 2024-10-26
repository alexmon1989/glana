from django.shortcuts import render

from .models import AboutPage


def index(request):
    """Отображает страницу."""
    page, created = AboutPage.objects.get_or_create()
    return render(request, 'about/index/index.html', {'page': page})
