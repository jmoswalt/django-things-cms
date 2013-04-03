import ConfigParser
from os import path

from johnny.cache import enable


def load_theme_snippets(theme_path):
    enable()
    Config = ConfigParser.ConfigParser()
    Config.read(path.join(theme_path, "theme.info"))
    if "snippets" in Config.sections():
        from snippets.models import Snippet
        options = Config.options("snippets")
        for opt in options:
            slug = opt.replace(' ', '-').lower()
            value = Config.get("snippets", opt)
            try:
                Snippet.objects.get(slug=slug)
            except Snippet.DoesNotExist:
                print "New Snippet found: ", opt.title()
                new_snippet = Snippet()
                new_snippet.name = opt.title()
                new_snippet.slug = slug
                new_snippet.values = {'content': value}
                new_snippet.save()
            except Exception as e:
                print e
