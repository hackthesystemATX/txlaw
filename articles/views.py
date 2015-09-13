from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
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
    articles = category.articles.all()
    resources = category.resources.all()
    return render(request, "results.html", {'articles': articles, 'resources': resources})

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