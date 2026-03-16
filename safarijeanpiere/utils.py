from django.urls import get_resolver, URLPattern, URLResolver
from safarijeanpiere.utils import list_routes


def list_routes():  # noqa: F811
    """
    Returns all registered Django routes with their URL pattern
    """
    resolver = get_resolver()
    routes = []

    def extract_patterns(urlpatterns, prefix=''):
        for pattern in urlpatterns:
            if isinstance(pattern, URLPattern):
                route = prefix + str(pattern.pattern)
                routes.append({
                    "path": route,
                    "name": pattern.name,
                    "callback": pattern.callback.__name__,
                })

            elif isinstance(pattern, URLResolver):
                extract_patterns(
                    pattern.url_patterns,
                    prefix + str(pattern.pattern)
                )

    extract_patterns(resolver.url_patterns)

    return routes
