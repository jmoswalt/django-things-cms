from things import attrs, types, models


POST_ATTRIBUTES = (
    attrs.IMAGE,
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


POST_PHOTO_ATTRIBUTES = (
    attrs.IMAGE,
    {
        "name": "Related Post",
        "key": "post",
        "description": "The Post related to the {{ model }}.",
        "datatype": types.TYPE_FOREIGNKEY,
        "required": True,
        "model": Post
    },
)


class PostPhoto(models.Thing):

    class Meta:
        proxy = True


models.register_thing(Post, POST_ATTRIBUTES)
models.register_thing(PostPhoto, POST_PHOTO_ATTRIBUTES)
