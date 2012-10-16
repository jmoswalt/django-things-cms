from django.contrib.contenttypes.models import ContentType
from django import forms

from things.models import Thing
from things.types import *

ARITCLE_ATTRIBUTES = (
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        "form_widget": forms.Textarea(),
        "required": True,
        "datatype": TYPE_TEXT
    },
    {
        "name": "Author",
        "key": "author",
        "description": "The Author of the Article.",
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
    def content_type(cls):
        return ContentType.objects.get(name="article", app_label="articles")

    # FIELD METHODS
    def published_at(self):
        return self.published_at

    def author(self):
        return self.author
