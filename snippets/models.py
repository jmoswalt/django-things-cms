from things.models import Thing, register_thing
from things import attrs


TEMPLATE_TEXT_ATTRIBUTES = (
    attrs.CONTENT,
)


class Snippet(Thing):

    class Meta:
        proxy = True


register_thing(Snippet, TEMPLATE_TEXT_ATTRIBUTES)
