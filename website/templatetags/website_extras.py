from django import template

register = template.Library()

@register.filter
def numberitems(value, arg):
    return 20 * (arg-1) + value