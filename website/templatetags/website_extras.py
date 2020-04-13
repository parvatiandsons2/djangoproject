
from django.utils.html import format_html
from django.template.library import Library


register = Library()

@register.filter
def htmlConvert(value, arg):
    return format_html(value)