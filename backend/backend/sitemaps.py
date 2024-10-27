from django.contrib import sitemaps
from django.urls import reverse
from apps.products.models import Product


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['home', 'contacts:index', 'contacts:index', 'contacts:index']

    def location(self, item):
        return reverse(item)

    alternates = True
    x_default = True
    i18n = True


class ProductsSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Product.objects.enabled()

    def lastmod(self, obj):
        return obj.updated_at
