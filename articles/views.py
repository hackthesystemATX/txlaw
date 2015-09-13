from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Category, Article, Resource
import operator

def landing(request):
    return render(request, "landing.html", {'categories': Category.objects.all()})

def search(request, id=None):
    query = request.POST['query']
    # TODO: use an actual search engine
    if id is not None:
        category = get_object_or_404(Catgory, pk=id)
        articles = (Article.objects.filter(title__icontains=query) | Article.objects.filter(text__icontains=query)).filter(categories__in=[category]).all()
        resources = (Resource.objects.filter(name__icontains=query) | Resource.objects.filter(description__icontains=query)).filter(categories__in=[category]).all()
    else:
        articles = (Article.objects.filter(title__icontains=query) | Article.objects.filter(text__icontains=query)).all()
        resources = (Resource.objects.filter(name__icontains=query) | Resource.objects.filter(description__icontains=query)).all()
    return render(request, "results.html", {'articles': articles, 'resources': resources})


def article(request, id):
    article = get_object_or_404(Article, pk=id)
    resources = {} # Key is resource, value is number of overlapping categories

    # Get all resources that share a category with the article.
    for category in article.categories.iterator(): # maybe filter by is_major
        for resource in category.resources.iterator():
            if resource not in resources:
                resources[resource] = 1
            else:
                resources[resource] += 1

    # Sort based on how many categories overlap
    resources_sorted = [res[0] for res in sorted(resources.items(), key=operator.itemgetter(1), reverse=True)]

    return render(request, "article.html", {'article': article, 'resources': resources_sorted})

def category(request, id):
    category = get_object_or_404(Category, pk=id)
    articles = category.articles.all()
    resources = category.resources.all()
    return render(request, "results.html", {'category': category, 'articles': articles, 'resources': resources})

def resources(request):
    return render(request, "resources.html", {'resources': Resource.objects.all(), 'categories': Category.objects.all()})

def category_resources(request, id):
    category = get_object_or_404(Category, pk=id)
    return render(request, "resources.html", {'resources': category.resources.all()})

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page
            return
        else:
            # Returns a 'disabled account' error
            return
    else:
        # Return 'invalid login'
        return

def logout_view(request):
    logout(request)
    # Redirect to success page
    return

def register_view(request):
    pass

# article editing view