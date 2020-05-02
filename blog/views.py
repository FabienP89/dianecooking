from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from blog.models import Post, Comment, Contact, Newsletter
from blog.forms import CreateCommentForm, ContactForm, NewsletterForm
from blog.utils import unique_slug_generator
from django.template.loader import render_to_string





def about(request):
    return HttpResponse('about page...')



def home(request, newsletter=''):
    posts = Post.objects.filter(published=True)
    preferred_posts = Post.objects.filter(published=True).order_by('-likes')[:5]
    unique_recent_post = Post.objects.filter(published=True).order_by('-created_at')[0]
    recent_posts_block1 = Post.objects.filter(published=True).order_by('-created_at')[1:5]
    recent_posts_block2 = Post.objects.filter(published=True).order_by('-created_at')[5:9]
    sliders = Post.objects.filter(published=True, slider_home_page=True).order_by('-created_at')
    if request.method == 'POST':    
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            newsletter = 'Merci ! Votre inscription à la newsletter est bien prise en compte !'
    else:
        newsletter_form = NewsletterForm()
        
        
    context = {
    'preferred_posts': preferred_posts,
    'posts' : posts,
    'unique_recent_post' : unique_recent_post,
    'recent_posts_block1': recent_posts_block1,
    'recent_posts_block2': recent_posts_block2,
    'sliders': sliders,
    'newsletter_form' : newsletter_form,
    'newsletter' : newsletter,
    }
    return render(request, 'blog/home.html', context)



def contact(request, message =''):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            message = 'Merci ! Je vous répondrai dans les meilleurs délais.'

    else:
        contact_form = ContactForm()
            
    context = {
    'contact_form' : contact_form,
    'message' : message,
    }
    return render(request, 'blog/contact.html', context)


def search(request):
    if request.method == 'GET':
        search_term = request.GET['search']
        if search_term :
            posts = Post.objects.filter(
                Q(title__icontains= search_term) |
                Q(introduction__icontains= search_term) |
                Q(citation__icontains= search_term) |
                Q(title_chapter1__icontains= search_term) |
                Q(ch1_block1__icontains= search_term) |
                Q(ch1_block2__icontains= search_term) |
                Q(ch1_block3__icontains= search_term) |
                Q(title_chapter2__icontains= search_term) |
                Q(ch2_block1__icontains= search_term) |
                Q(category__name__icontains= search_term)|
                Q(ingredients__ingredient__icontains= search_term)|
                Q(mealtype__name__icontains= search_term)
            ).distinct()

    
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Résultats de recherche"
    
    context = {
    'search_term' : search_term,
    'posts' : posts,
    'page_posts' : page_posts,
    'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)




def savory_recipes(request):
    posts = Post.objects.filter(category__name__iexact="recettes salées").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Recettes salées"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def aperitifs(request):
    posts = Post.objects.filter(mealtype__name__iexact="apéritifs").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Apéritifs"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def entrees(request):
    posts = Post.objects.filter(mealtype__name__iexact="entrées").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Entrées"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)


def viandes(request):
    posts = Post.objects.filter(mealtype__name__iexact="viandes").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Viandes"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)


def tartes_quiches(request):
    posts = Post.objects.filter(mealtype__name__iexact="tartes/quiches").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Tartes/Quiches"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def poissons(request):
    posts = Post.objects.filter(mealtype__name__iexact="poissons").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Poissons"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)


def accompagnements(request):
    posts = Post.objects.filter(mealtype__name__iexact="accompagnements").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Accompagnements"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def boulange(request):
    posts = Post.objects.filter(mealtype__name__iexact="boulange").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Boulange"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def sweet_recipes(request):
    posts = Post.objects.filter(category__name__iexact="recettes sucrées").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Recettes sucrées"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)


def gateaux(request):
    posts = Post.objects.filter(mealtype__name__iexact="gâteaux").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Gâteaux"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def goutes(request):
    posts = Post.objects.filter(mealtype__name__iexact="goûtés").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Goûtés"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def viennoiseries(request):
    posts = Post.objects.filter(mealtype__name__iexact="viennoiseries").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Viennoiseries"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def tartes(request):
    posts = Post.objects.filter(mealtype__name__iexact="tartes").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Tartes"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def desserts_individuels(request):
    posts = Post.objects.filter(mealtype__name__iexact="desserts individuels").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Desserts individuels"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)


# recettes par thèmes

def theme_recipes(request):
    posts = Post.objects.filter(category__name__iexact="recettes par thème").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Recettes par thème"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)

def paques(request):
    posts = Post.objects.filter(mealtype__name__iexact="pâques").order_by('-created_at')
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    name = "Pâques"
    context = {
            'posts' : posts,
            'page_posts' : page_posts,
            'name' : name,
    }
    return render(request, 'blog/all_recipes.html', context)



def recipe(request, slug, message=''):
    post = get_object_or_404(Post, slug=slug)
    preferred_posts = Post.objects.filter(published=True).order_by('-likes')[:5]
    posts_same_category = Post.objects.filter(category__in=post.category.all(), published=True).exclude(slug=slug)
    comments = post.comments.filter(parent__isnull=True).exclude(status=Comment.STATUS_HIDDEN).order_by('created_at')
    newsletter = ''
    
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            newsletter = 'Merci ! Votre inscription à la newsletter est bien prise en compte !'

    else:
        newsletter_form = NewsletterForm()
    
    if request.method == 'POST' and not newsletter_form.is_valid():
        comment_form = CreateCommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id :
                parent_obj= Comment.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            message = 'Votre commentaire a bien été enregistré !'
            
    else : 
        comment_form = CreateCommentForm()

    
            
    context = {
        'post': post,
        'preferred_posts' : preferred_posts,
        'posts_same_category': posts_same_category,
        'comments': comments,
        'comment_form': comment_form,
        'newsletter_form': newsletter_form,
        'message': message,
        'newsletter': newsletter,
    }
    return render(request, 'blog/recipe.html', context)


        

def like_post(request):
    post_id = None

    # Getting the id of the post from the template
    if request.method == 'GET':
        post_id = request.GET['post_id']

    likes = 0

    if post_id:
        post = Post.objects.get(id = int(post_id))
        if post:
            likes = post.likes + 1
            post.likes = likes
            post.save()

    return HttpResponse(likes)



"""
def likes_post(request):

    # Getting the id of the post from the template
    if request.method == 'POST':
        post_id = request.POST['post_id']

    if post_id:
        post = Post.objects.get(id = int(post_id))
        if post:
            likes = post.likes + 1
            post.likes = likes
            post.save()

    return HttpResponse(likes)
    """

def comment_like(request):
    comment_id = None

    # Getting the id of the post from the template
    if request.method == 'GET':
        comment_id = request.GET['comment_id']

    likes = 0

    if comment_id:
        comment = Comment.objects.get(id = int(comment_id))
        if comment:
            likes = comment.likes + 1
            comment.likes = likes
            comment.save()

    return HttpResponse(likes)