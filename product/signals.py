from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Recipe
from slugify import slugify


@receiver(post_save, sender=Recipe)
def my_handler(sender,instance,created,**kwargs):
    if created:
        instance.slug=slugify(instance.title)
        instance.save()
      
      
        
        
            

    
    