from django.contrib import admin
from django.db import models
from django.forms import Textarea
from blog.models import PostCategory, Post, Comment, Ingredient, Contact, MealType, Newsletter
import datetime


class DianeCookingAdminSite(admin.AdminSite):
    site_header = "Administration Diane Cooking"

admin_site = DianeCookingAdminSite(name='admin')


@admin.register(PostCategory, site=admin_site)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Post, site=admin_site)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published',
        'created_at',
        'comments_count',
    )
    
    autocomplete_fields = ['category', 'ingredients', 'mealtype']
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols': 120})}
        }
    
    list_filter = (
        'category__name',
        'published',
    )
    
    def comments_count(self, obj):
        return Comment.objects.filter(post=obj).count()
    comments_count.short_description = "Comments"

    search_fields = ["title"]

@admin.register(Comment, site=admin_site)    
class CommentAdmin(admin.ModelAdmin):
    
    search_fields = ['post__title', 'author_name',]
    list_display = (
        'post',
        'author_name',
        'status',
        'moderation_text',
        'created_at',
        'text',
    )
    
    list_editable = ('status', 'moderation_text',)
    
    list_filter = ('status',)
    
    
@admin.register(Ingredient, site=admin_site)    
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['ingredient']



@admin.register(Contact, site=admin_site)
class ContactAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return obj.created_at.strftime("%d %b %Y %H:%M:%S")  
    time_seconds.admin_order_field = 'created_at'
    list_display = ('name', 'email', 'created_at' )

@admin.register(MealType, site=admin_site)
class MealTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
@admin.register(Newsletter, site=admin_site)
class NewsletterAdmin(admin.ModelAdmin):
    search_fields = ['email']