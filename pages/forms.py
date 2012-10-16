from things.forms import ThingForm
from pages.models import Page


class PageForm(ThingForm):
    model = Page
