from django.template import Library
from product.models import Category


register=Library()

@register.simple_tag
def get_categories(limit):
    category=Category.objects.all()[:limit]

    return category

@register.inclusion_tag("includes/recent_blogs.html")
def recent_blogs():
     category=Category.objects.all()

     return {
          "categories":category
     }




