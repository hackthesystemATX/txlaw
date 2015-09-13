from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.TextField(blank=True)
    # Should this category be shown on the main page?
    is_major = models.BooleanField(default=False)

    # articles: related field for Article.categories
    # resources: related field for Resource.categories

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    author = models.ForeignKey(User)
    text = models.TextField()
    categories = models.ManyToManyField(Category, related_name='articles')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    '''
    A resource for users, such as lawyers' offices, domestic violence shelters, tenants' groups, etc.
    '''
    name = models.CharField(max_length=50)
    summary = models.TextField()
    description = models.TextField()

    address = models.TextField(blank=True)
    # If False, the resource is something like a phone hotline, and shouldn't be filtered by location.
    location_based = models.BooleanField(default=True)

    url = models.URLField(blank=True)
    phone = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True)

    categories = models.ManyToManyField(Category, related_name='resources')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    organization = models.TextField(blank=True)
    # i.e. "Law Student" or "Texas Lawyer"
    legal_desc = models.TextField(blank=True, max_length=50)
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        name = "%s %s" % (self.user.first_name, self.user.last_name)
        if self.legal_desc is not None and len(self.legal_desc) > 0:
            name = name + ", " + legal_desc
        if self.organization is not None and len(self.organization) > 0:
            name = name + " (" + self.organization + ")"
        return name
