from django.template import Library


register=Library()

@register.filter
def truncate(text):
    result=text.split(".")[0]
   
    return result

