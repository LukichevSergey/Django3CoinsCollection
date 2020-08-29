from django import template

from ..models import Group

register = template.Library()

@register.inclusion_tag('collection/sidebar_tpl.html')
def show_group():
    groups = Group.objects.all()
    return {"groups": groups}