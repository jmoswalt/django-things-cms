from django.contrib.contenttypes.models import ContentType

from things.models import Thing
from things.types import *

PAGE_ATTRIBUTES = (
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        "datatype": TYPE_TEXT
    },
    {
        "name": "Private",
        "key": "private",
        "description": "Select whether or not this is a private Page.",
        "datatype": TYPE_BOOLEAN
    },
    {
        "name": "Priority",
        "key": "priority",
        "description": "Select whether or not this is a private Page.",
        "datatype": TYPE_INT
    },
)


class Page(Thing):

    class Meta:
        proxy = True

    @classmethod
    def attrs(cls):
        return PAGE_ATTRIBUTES

    @classmethod
    def content_type(cls):
        return ContentType.objects.get(name="page", app_label="pages")
