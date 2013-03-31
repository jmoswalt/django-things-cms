from things.models import Thing, register_thing
from things import attrs


TEMPLATE_TEXT_ATTRIBUTES = (
    attrs.CONTENT,
)


class Snippet(Thing):

    class Meta:
        proxy = True

    def template_tag(self):
        if self.slug:
            return '_'.join(['s', self.slug.replace('-', '_')]).upper()
        return ""

register_thing(Snippet, TEMPLATE_TEXT_ATTRIBUTES)
