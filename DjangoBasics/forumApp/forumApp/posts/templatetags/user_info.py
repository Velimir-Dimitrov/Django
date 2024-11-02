from django import template

register = template.Library()

@register.inclusion_tag("common/user_info.html") #takes_context=True option available
def user_info(user):
    if user.is_authenticated:
        return {"username": user}
    return {"username": "Anonymous"}