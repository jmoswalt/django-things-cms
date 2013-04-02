from things.forms import ThingForm
from .models import Post


class PostForm(ThingForm):
    model = Post
