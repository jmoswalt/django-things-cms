from django.contrib.contenttypes.models import ContentType

from things.models import Thing, register_thing
from things.types import *

ARITCLE_ATTRIBUTES = (
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        "required": True,
        "datatype": TYPE_LONGTEXT
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
    def content_type(cls):
        return ContentType.objects.get(name="article", app_label="articles")

register_thing(Article, ARITCLE_ATTRIBUTES)
