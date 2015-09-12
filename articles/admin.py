from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Article, Resource, Profile

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
	inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Resource)
