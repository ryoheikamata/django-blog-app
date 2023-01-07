from django import template

register = template.Library()

@register.simple_tag
def replace(requesst, key, value):
    url_dict = requesst.GET.copy()
    url_dict[key] = value

    return url_dict.urlencode()

