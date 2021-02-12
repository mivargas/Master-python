from blog.models import Category, Article

def get_categories(request):
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True) #consutar los id de categorias que tengan articulos (esten publicadas)

    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name') # el filtro es para indicarle que los id que esten en la consulta anterior (seria algo equivalente a 'SELECT id, name  from caregory WHERE id in({categories_in_use})')

    return {
        'categories': categories
    }