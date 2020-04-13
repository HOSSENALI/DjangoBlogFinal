from django.contrib import admin
from BlogApp.models import author, category, article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'title', 'body', 'category']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'details']


admin.site.register(author,AuthorAdmin)
admin.site.register(category)
admin.site.register(article,ArticleAdmin)
