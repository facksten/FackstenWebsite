from django.contrib import admin
from .models import (
    ArticleCategory, Article
)
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'created_at' , 'rate' , 'slug')
admin.site.register(Article, ArticleAdmin)

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title' , 'created_at')
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

