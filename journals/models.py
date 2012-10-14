from django.db import models
from django.core.urlresolvers import reverse

from things.models import Thing
from things.types import *

JOURNAL_ATTRIBUTES = (
    {
        "name": "Author",
        "key": "author",
        "description": "The Author of the Journal.",
        "datatype": TYPE_TEXT
    },
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        "datatype": TYPE_TEXT
    },
    {
        "name": "Journal Date",
        "key": "journal_date",
        "description": "The publish date of the Journal.",
        "datatype": TYPE_DATE
    },
    {
        "name": "Personal",
        "key": "personal",
        "description": "Select whether or not this is a personal Journal.",
        "datatype": TYPE_BOOLEAN
    },
    {
        "name": "Day Weather",
        "key": "temperature",
        "description": "The temperature for this Journal (in F).",
        "datatype": TYPE_FLOAT
    },
)


class Journal(Thing):

    class Meta:
        proxy = True

    @classmethod
    def attrs(cls):
        return JOURNAL_ATTRIBUTES

    @classmethod
    def clstype(cls):
        return "journal"

    @models.permalink
    def get_absolute_url(self):
        return ("journal_detail", [self.slug])

    def get_edit_url(self):
        return reverse("admin:journals_journal_change", args=[self.pk])
