from django import template

register = template.Library()

@register.simple_tag
def active(name, title):
    if name == title.lower():
        return "active"
    return ""

@register.filter
def typeof(variable):
    return type(variable).__name__

