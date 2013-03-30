from things.models import Thing, register_thing
from things import attrs


ARITCLE_ATTRIBUTES = (
    attrs.CONTENT,
    attrs.AUTHOR,
    attrs.PUBLISHED_AT,
    attrs.FEATURED,
)


class Article(Thing):

    class Meta:
        proxy = True


register_thing(Article, ARITCLE_ATTRIBUTES)
