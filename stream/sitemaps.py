from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'login', 'anime-details', 'anime-watch', 'search']
    def location(self, item):
        return reverse(item)
