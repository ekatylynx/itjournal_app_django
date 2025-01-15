from News.models import Category
from django import template

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()