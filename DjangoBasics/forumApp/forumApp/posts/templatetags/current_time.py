import datetime
from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string="%Y-%m-%d %I:%M %p"):
    return datetime.datetime.now().strftime(format_string)