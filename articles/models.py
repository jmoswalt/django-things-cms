from django.db import models
from django.core.urlresolvers import reverse

from things.models import Thing
from things.types import *

ARITCLE_ATTRIBUTES = (
    {
        "name": "Author",
        "key": "author",
        "description": "The Author of the Article.",
        "datatype": TYPE_TEXT
    },
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        "datatype": TYPE_TEXT
    },
    {
        "name": "Publish Date",
        "key": "published_at",
        "description": "The publish date of the Article.",
        "datatype": TYPE_DATE
    },
    {
        "name": "Featured",
        "key": "featured",
        "description": "Select whether or not this is a featured Article.",
        "datatype": TYPE_BOOLEAN
    },
    # {
    #     "name": "My Float",
    #     "key": "my_float",
    #     "description": "The publish date of the Article.",
    #     "datatype": TYPE_FLOAT
    # },
    # {
    #     "name": "My Int",
    #     "key": "my_int",
    #     "description": "The publish date of the Article.",
    #     "datatype": TYPE_INT
    # },
)


class ArticleManager(models.Manager):
    def get_query_set(self):
        return super(ArticleManager, self).get_query_set().filter(type="article")


class Article(Thing):
    objects = ArticleManager()

    class Meta:
        proxy = True

    def attrs(self):
        return ARITCLE_ATTRIBUTES

    def save(self, *args, **kwargs):
        self.type = "article"
        super(Article, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("article_detail", [self.slug])

    def get_edit_url(self):
        return reverse("admin:articles_article_change", args=[self.pk])
