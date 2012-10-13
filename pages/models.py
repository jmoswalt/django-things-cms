from django.db import models
from django.core.urlresolvers import reverse

from things.models import Thing
from things.types import *

ARITCLE_ATTRIBUTES = (
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
)


class PageManager(models.Manager):
    def get_query_set(self):
        return super(PageManager, self).get_query_set().filter(type="page")


class Page(Thing):
    objects = PageManager()

    class Meta:
        proxy = True

    def attrs(self):
        return ARITCLE_ATTRIBUTES

    def save(self, *args, **kwargs):
        self.type = "page"
        super(Page, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("page_detail", [self.slug])

    def get_edit_url(self):
        return reverse("admin:pages_page_change", args=[self.pk])
