from datetime import datetime

from things import attrs, types, models


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


class Article(models.Thing):
    public_filter_out = {
        'published_at__gte': 0,
        'published_at__lte': datetime.now().replace(second=0, microsecond=0)
    }
    super_user_order = ['-published_at', '-created_at']
    public_order = "-published_at"

    class Meta:
        proxy = True


models.register_thing(Article, ARITCLE_ATTRIBUTES)
