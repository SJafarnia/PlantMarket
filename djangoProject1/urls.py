from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .views import ProductSitemap
from django.contrib import admin
from django.contrib.sitemaps import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': {"products": ProductSitemap}},
    name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
    path('', include("products.urls")),
    path('orders/', include("orders.urls")),
    path('auth/', include('users.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
