from things.models import Thing, register_thing
from things import attrs, types


ARITCLE_ATTRIBUTES = (
    attrs.CONTENT,
    attrs.AUTHOR,
    {
        "name": "Mood",
        "key": "mood",
        "description": "The mood for the author.",
        "datatype": types.TYPE_TEXT
    },
    attrs.PUBLISHED_AT,
    attrs.FEATURED,
)


class Article(Thing):

    class Meta:
        proxy = True


register_thing(Article, ARITCLE_ATTRIBUTES)
