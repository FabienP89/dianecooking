import random
import os
from django.db import models
from django.urls import reverse
from datetime import date
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize
from imagekit.models import ProcessedImageField
from blog.utils import unique_slug_generator
from django.db.models.signals import pre_save


class PostCategory(models.Model):
    name = models.CharField(max_length=100)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "catégorie"
        
        
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    category = models.ManyToManyField('PostCategory', blank=True)
    mealtype = models.ManyToManyField('MealType', blank=True)
    ingredients = models.ManyToManyField('Ingredient', blank=True)
    published = models.BooleanField(default=False)
    introduction = models.TextField(blank=True, null=True)
    citation = models.TextField(blank=True)
    video = models.URLField(blank=True, null=True)
    title_chapter1 = models.CharField(max_length=100, blank=True, null=True)
    ch1_block1 = models.TextField(blank=True, null=True)
    ch1_block2 = models.TextField(blank=True, null=True)
    ch1_block3 = models.TextField(blank=True, null=True)
    title_chapter2 = models.CharField(max_length=100, blank=True, null=True)
    ch2_block1 = models.TextField(blank=True, null=True)
    
    likes = models.IntegerField(default=0)
    slider_home_page = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(default='default.jpg')
    cover_image_thumbnail =ImageSpecField(source='cover_image', processors = [Transpose()], format = 'JPEG', options = {'quality': 90})
    image1 = models.ImageField(default='default.jpg')
    image_thumbnail1 =ImageSpecField(source='image1', processors = [Transpose()], format = 'JPEG', options = {'quality': 90})
    image2 = models.ImageField(default='default.jpg')
    image_thumbnail2 = ImageSpecField(source='image2', processors = [Transpose()], format = 'JPEG', options = {'quality': 90})
    image3 = models.ImageField(default='default.jpg')
    image_thumbnail3 = ImageSpecField(source='image3', processors = [Transpose(),], format = 'JPEG', options = {'quality': 90})
    image4 = models.ImageField(default='default.jpg')
    image_thumbnail4 = ImageSpecField(source='image4', processors = [Transpose(),], format = 'JPEG', options = {'quality': 90})
    image5 = models.ImageField(default='default.jpg')
    image_thumbnail5 = ImageSpecField(source='image5', processors = [Transpose(),], format = 'JPEG', options = {'quality': 90})
    image_slider = models.ImageField(default='default.jpg')
    image_thumbnail_slider = ImageSpecField(source='image_slider', processors = [Transpose(), ResizeToFill(601,902)], format = 'JPEG', options = {'quality': 90})
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save()
        
        
    class Meta:
        verbose_name = "recette"

    def get_absolute_url(self):
        return reverse('recette', kwargs={"slug":self.slug})
        

    """
    def get_absolut_url(self):
        return reverse('post', args=[str(self.slug)])
  

    def get_absolut_url(self):
        return f'/{self.slug}/'
    """

    
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)
            
pre_save.connect(slug_generator, sender= Post)  


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=500)

    def __str__(self):
        return self.ingredient


class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_MODERATED, 'Moderated'),
    )

    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20,default=STATUS_VISIBLE, choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return '{} - {} (status={})'.format(self.author_name, self.text[:20], self.status)
    class Meta:
        verbose_name = "commentaire"
    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    compagny = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.name} - {self.email}'
    
    
class MealType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
         return f'{self.name}'
    
    class Meta:
        verbose_name = "sous-catégorie"
     
class Newsletter(models.Model):
    email = models.EmailField(max_length=200)
    
    def __str__(self):
        return f'{self.email}'