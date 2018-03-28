from django.urls import path, include
from django.contrib import admin

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from main.models import Name

info_dict = {
    'queryset': Name.objects.all()
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sitemap.xml',
        sitemap,
        {'sitemaps':
            {
                'names': GenericSitemap(info_dict, priority=0.6)
            }
         },
        name='django.contrib.sitemaps.views.sitemap')
]
