from django.template import Library
from django.utils.safestring import mark_safe

from snippets.models import Snippet

register = Library()


@register.inclusion_tag('_snippet.html', takes_context=True)
def snippet(context, slug, safe=False):
    context.update({
        'snippet_obj': None,
        'snippet_content': None
    })

    try:
        snippet = Snippet.objects.get(slug=slug)
        content = snippet.content
        if safe:
            content = mark_safe(snippet.content)
        context.update({
            'snippet_obj': snippet,
            'snippet_content': content
        })
    except Snippet.DoesNotExist:
        pass

    return context
