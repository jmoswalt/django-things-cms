from things.models import Thing, register_thing
from things import attrs, types


POST_ATTRIBUTES = (
    {
        "name": "Featured Image",
        "key": "featured_image",
        "description": "Add a featured image to the {{ model }}.",
        "datatype": types.TYPE_FILE
    },
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
