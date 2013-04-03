from things.forms import ThingForm
from .models import Snippet


class SnippetForm(ThingForm):
    model = Snippet
