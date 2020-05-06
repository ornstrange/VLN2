from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    request = context['request']
    updated = request.GET.copy()
    for param, value in kwargs.items():
        updated[param] = value
    return f"?{updated.urlencode()}" if updated else ''

