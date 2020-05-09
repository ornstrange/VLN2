from django import template

register = template.Library()

@register.simple_tag
def active(name, title):
    if type(name) in [tuple, list]:
        if title.lower() in name:
            return "active"
    if name == title.lower():
        return "active"
    return ""

@register.filter
def typeof(variable):
    return type(variable).__name__

