from django.contrib.contenttypes.models import ContentType

from things.models import Thing, register_thing
from things.types import *

PAGE_ATTRIBUTES = (
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        "required": True,
        "datatype": TYPE_LONGTEXT
    },
    {
        "name": "Private",
        "key": "private",
        "description": "Select whether or not this is a private Page.",
        "datatype": TYPE_BOOLEAN
    },
)


class Page(Thing):

    class Meta:
        proxy = True

    @classmethod
    def content_type(cls):
        return ContentType.objects.get(name="page", app_label="pages")

register_thing(Page, PAGE_ATTRIBUTES)
