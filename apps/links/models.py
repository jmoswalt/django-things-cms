from things.models import Thing, register_thing
from things import attrs, types


LINK_ATTRIBUTES = (
    attrs.CONTENT,
    {
        "name": "Link URL",
        "key": "link_url",
        "description": "The URL of the {{ model }}.",
        "required": True,
        "datatype": types.TYPE_TEXT
    },
    {
        "name": "Source Name",
        "key": "source_name",
        "description": "The name of the source for the {{ model }}.",
        "datatype": types.TYPE_TEXT
    },
    {
        "name": "Source URL",
        "key": "source_url",
        "description": "The url of the source for the {{ model }}.",
        "datatype": types.TYPE_TEXT
    },
    attrs.PUBLISHED_AT,
    attrs.PRIVATE,
)


class Link(Thing):

    class Meta:
        proxy = True


register_thing(Link, LINK_ATTRIBUTES)
