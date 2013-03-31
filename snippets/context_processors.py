from .models import Snippet


def snippets(request):
    """
        Context processor for snippets
    """

    contexts = {}
    for snippet in Snippet.objects.all():
        contexts[snippet.template_tag()] = snippet.content

    return contexts
