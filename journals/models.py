from django.contrib.contenttypes.models import ContentType

from things.models import Thing, register_thing
from things.types import *

JOURNAL_ATTRIBUTES = (
    {
        "name": "Content",
        "key": "content",
        "description": "The main content of the ariticle.",
        # "form_widget": forms.Textarea(),
        "required": True,
        "datatype": TYPE_LONGTEXT
    },
    {
        "name": "Author",
        "key": "author",
        "description": "The Author of the Journal.",
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
    def content_type(cls):
        return ContentType.objects.get(name="journal", app_label="journals")

register_thing(Journal, JOURNAL_ATTRIBUTES, ContentType.objects.get(name="journal", app_label="journals"))
