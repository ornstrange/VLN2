from django import template

register = template.Library()

@register.simple_tag
def active(name, title):
    if type(name) in [tuple, list]:
        for n in name:
            if type(n) == dict:
                if title.lower() in n.values():
                    return "active"
            elif title.lower() == n:
                return "active"
    if type(name) == dict:
        if title.lower() in name.values():
            return "active"
    if name == title.lower():
        return "active"
    return ""

@register.filter
def typeof(variable):
    return type(variable).__name__

