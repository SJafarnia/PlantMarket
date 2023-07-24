from django.contrib.sitemaps import Sitemap

from products.models import Product


class ProductSitemap(Sitemap):
    name = 'product'
    changefreq = 'daily'
    limit = 50000

    def items(self):
        return  Product.objects.order_by('id')