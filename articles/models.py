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
    #     "name": "Order",
    #     "key": "ordering",
    #     "description": "The order number of the Article.",
    #     "datatype": TYPE_INT
    # },
)


class Article(Thing):

    class Meta:
        proxy = True

    @classmethod
    def attrs(cls):
        return ARITCLE_ATTRIBUTES

    @classmethod
    def clstype(cls):
        return "article"

    @models.permalink
    def get_absolute_url(self):
        return ("article_detail", [self.slug])

    def get_edit_url(self):
        return reverse("admin:articles_article_change", args=[self.pk])

    # FIELDS
    def published_at(self):
        return self.published_at

    def author(self):
        return self.author
