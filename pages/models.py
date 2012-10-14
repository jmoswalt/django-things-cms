from django.db import models
from django.core.urlresolvers import reverse

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
    def clstype(cls):
        return "page"

    @models.permalink
    def get_absolute_url(self):
        return ("page_detail", [self.slug])

    def get_edit_url(self):
        return reverse("admin:pages_page_change", args=[self.pk])
