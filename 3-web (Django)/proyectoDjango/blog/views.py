from django.shortcuts import render, get_object_or_404 #devolver 404 
from .models import Category, Article
from django.core.paginator import Paginator #libreria para paginar elementos
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login") 
def list(request):
    #sacar  articulos
    articles = Article.objects.all()

    #paginar articulos
    paginator = Paginator(articles, 2)

    #Recoger numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request,'articles/list.html', {
        'title':'Articulos',
        'articles': page_articles
    })

@login_required(login_url="login") 
def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id) #aqui se devuelveun 404 si no existe la categoria
    #articles = Article.objects.filter(categories=category_id) # category_id o category puesdo pasarle id #no hace falta ya que se puede hacer un whit en la plantilla de iteracion de article la llamada a la relacion inversa por el ManyToMany

    return render(request, 'categories/category.html',{
        'category': category,
        #'articles': articles #se llama la relacion a la inversa
    })

@login_required(login_url="login") 
def article(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })

