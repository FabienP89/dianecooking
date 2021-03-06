"""blog_diane_cooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from blog.admin import admin_site

from django.conf.urls import url, include

from django.conf.urls.static import static

from blog.sitemaps import StaticViewSitemap, PostSitemap
from django.views.generic import TemplateView

sitemaps = {
    'posts': PostSitemap,
    'static' : StaticViewSitemap
}

TemplateView.as_view(template_name='blog/instagram.html', extra_context={
        "instagram_profile_name": "dianecooking"})

urlpatterns = [
    path('admin/', admin_site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('about/', views.about, name='about'),
    path('', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)