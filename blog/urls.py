from django.contrib import admin
from django.urls import path
from django.conf import settings
from blog.admin import admin_site
from blog import views
from django.conf.urls import url, include


urlpatterns = [
    path('', views.home, name='home'),
    path('/<str:newsletter>/', views.home, name='newsletter-subscrire'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
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
    path('tartes-quiches-cakes/', views.tartes_quiches_cakes, name='tartes_quiches_cakes'),
    path('pates/', views.pates, name='pates'),
    path('poissons/', views.poissons, name='poissons'),
    path('accompagnements/', views.accompagnements, name='accompagnements'),
    path('boulange/', views.boulange, name='boulange'),
    path('gateaux/', views.gateaux, name='gateaux'),
    path('goutes/', views.gouters, name='gouters'),
    path('viennoiseries/', views.viennoiseries, name='viennoiseries'),
    path('desserts-individuels/', views.desserts_individuels, name='desserts_individuels'),
    path('tartes/', views.tartes, name='tartes'),
    path('paques/', views.paques, name='paques'),
    path('<slug:slug>/', views.recipe, name='recette'),
]