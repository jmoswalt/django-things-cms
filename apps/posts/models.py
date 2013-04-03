from things import attrs, types, models


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


class Post(models.Thing):

    class Meta:
        proxy = True


models.register_thing(Post, POST_ATTRIBUTES)
