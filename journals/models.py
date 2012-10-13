from django.db import models
from django.core.urlresolvers import reverse

from things.models import Thing
from things.types import *

ARITCLE_ATTRIBUTES = (
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


class JournalManager(models.Manager):
    def get_query_set(self):
        return super(JournalManager, self).get_query_set().filter(type="journal")


class Journal(Thing):
    objects = JournalManager()

    class Meta:
        proxy = True

    def attrs(self):
        return ARITCLE_ATTRIBUTES

    def save(self, *args, **kwargs):
        self.type = "journal"
        super(Journal, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("journal_detail", [self.slug])

    def get_edit_url(self):
        return reverse("admin:journals_journal_change", args=[self.pk])
