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


sitemaps = {
    'posts': PostSitemap,
    'static' : StaticViewSitemap
}


urlpatterns = [
    path('admin/', admin_site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('/<str:newsletter>/', views.home, name='newsletter-subscrire'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('contact/<str:message>/', views.contact, name='confirmation-contact'),
    path('like_post/', views.like_post, name='like_post'),
    # path('likes_post/', views.likes_post, name='likes_post'),
    path('likes_comments/', views.comment_like, name='likes_comments'),
    # path('recettes/', views.all_recipes, name='recettes'),
    path('recettes-salees/', views.savory_recipes, name='recettes-salees'),
    path('recettes-sucrees/', views.sweet_recipes, name='recettes-sucrees'),
    path('recettes-par-theme/', views.theme_recipes, name='recettes-par-theme'),
    path('aperitifs/', views.aperitifs, name='aperitifs'),
    path('entrees/', views.entrees, name='entrees'),
    path('viandes/', views.viandes, name='viandes'),
    path('tartes-quiches/', views.tartes_quiches, name='tartes_quiches'),
    path('poissons/', views.poissons, name='poissons'),
    path('accompagnements/', views.accompagnements, name='accompagnements'),
    path('boulange/', views.boulange, name='boulange'),
    path('gateaux/', views.gateaux, name='gateaux'),
    path('goutes/', views.goutes, name='goutes'),
    path('viennoiseries/', views.viennoiseries, name='viennoiseries'),
    path('desserts-individuels/', views.desserts_individuels, name='desserts_individuels'),
    path('tartes/', views.tartes, name='tartes'),
    path('paques/', views.paques, name='paques'),
    path('<slug:slug>/', views.recipe, name='recette'),
    # path('<slug:slug>/<str:newsletter>/', views.recipe, name='confirmation-newsletter'),
    path('<slug:slug>/<str:message>/', views.recipe, name='confirmation-message'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)