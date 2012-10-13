from django.contrib import admin
from django.utils.text import truncate_words

from things.admin import ThingAdmin

from articles.forms import ArticleForm
from articles.models import Article


class ArticleAdmin(ThingAdmin):
    form = ArticleForm
    list_display = ['name', 'link', 'content', 'author', 'created_at']

    def content(self, obj):
        return truncate_words(obj.content, 15)

    def author(self, obj):
        return obj.author

admin.site.register(Article, ArticleAdmin)
