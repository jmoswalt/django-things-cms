from .models import TemplateText


def template_texts(request):
    """
        Context processor for template_texts
    """

    contexts = {}
    for tt in TemplateText.objects.all():
        contexts[tt.template_tag()] = tt.content

    return contexts
