from django import template

register = template.Library()

@register.filter()
def set_placeholder(value, placeholder):
    value.field.widget.attrs['placeholder'] = placeholder
    return value