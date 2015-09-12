from django.shortcuts import render, get_object_or_404
from .models import Category, Article, Resource

def landing(request):
    return render(request, "landing.html", {'categories': Category.objects.all()})

def search(request):
    query = request.POST['query']
    # TODO: use an actual search engine
    articles = (Article.objects.filter(title__icontains=query) | Article.objects.filter(text__icontains=query)).all()
    resources = (Resource.objects.filter(name__icontains=query) | Resource.objects.filter(description__icontains=query)).all()
    return render(request, "results.html", {'articles': articles, 'resources': resources})

def article(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, "article.html", {'article': article})

def resource(request, id):
    resource = get_object_or_404(Resource, pk=id)
    return render(request, "resource.html", {'resource': resource})

def category(request, id):
    category = get_object_or_404(Category, pk=id)
    return render(request, "category.html", {'category': category})

def login(request):
    pass

def logout(request):
    pass

def register(request):
    pass

# article editing view