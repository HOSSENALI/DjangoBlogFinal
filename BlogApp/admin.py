from django.contrib import admin
from BlogApp.models import author, category, article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'title', 'posted_on', 'category']
    search_fields = ['__str__']
    list_per_page = 10
    list_filter = ['posted_on', 'category']


admin.site.register(article, ArticleAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'details']
    search_fields = ['__str__']
    list_per_page = 10


admin.site.register(author, AuthorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['__str__']
    list_per_page = 10


admin.site.register(category, CategoryAdmin)
