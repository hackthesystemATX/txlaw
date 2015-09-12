from django.shortcuts import render
from .models import Category, Article, Resource

def landing(request):
    return render(request, "landing.html")

def search(request):
    query = request.POST['query']
    # TODO: use an actual search engine
    articles = Article.objects.all()
    resources = Resource.objects.all()
    return render(request, "results.html", {'articles': articles, 'resources': resources})

def article(request, id):
    pass

def resource(request, id):
    pass

def category(request, id):
    pass

def login(request):
    pass

def logout(request):
    pass

def register(request):
    pass

# article editing view