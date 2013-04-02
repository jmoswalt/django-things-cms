from things.models import Thing, register_thing
from things import attrs, types


POST_ATTRIBUTES = (
    attrs.CONTENT,
    {
        "name": "Tags",
        "key": "tags",
        "description": "Add some tags for our {{ model }}.",
        "datatype": types.TYPE_TEXT
    },
    attrs.PUBLISHED_AT,
    attrs.FEATURED,
)


class Post(Thing):

    class Meta:
        proxy = True


register_thing(Post, POST_ATTRIBUTES)
