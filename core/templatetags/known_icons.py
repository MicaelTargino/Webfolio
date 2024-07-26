from django import template

register = template.Library()

@register.filter
def get_icon(known_icons, key):
    return known_icons.get(key, '')