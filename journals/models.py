from things.models import Thing, register_thing
from things.types import *
from things import attrs


JOURNAL_ATTRIBUTES = (
    attrs.CONTENT,
    attrs.AUTHOR,
    attrs.PUBLISHED_AT,
    attrs.PRIVATE,
    {
        "name": "Day Weather",
        "key": "temperature",
        "description": "The temperature for this {{ model }} (in F).",
        "datatype": TYPE_FLOAT
    },
)


class Journal(Thing):

    class Meta:
        proxy = True


register_thing(Journal, JOURNAL_ATTRIBUTES)
