from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["home",]

    def location(self, item):
        return reverse(item)

    alternates = True
    x_default = True
    i18n = True
