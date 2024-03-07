from collections.abc import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify
from django.urls import reverse_lazy

User=get_user_model()


class AbstractClass(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract=True


class Category(AbstractClass):
    title=models.CharField(max_length=100)
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name_plural="Categories"
        


    def __str__(self):

        return f"{self.parent}-{self.title}"
    



class Tag(AbstractClass):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class RecipeImages(AbstractClass):
    image=models.ImageField(upload_to="images")
    recipe=models.ForeignKey("Recipe",on_delete=models.CASCADE,related_name="recipe")


class RecipeReview(AbstractClass):
    message=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews")
    recipe=models.ForeignKey("Recipe",on_delete=models.CASCADE,related_name="recipe_reviews")

class Recipe(AbstractClass):
    title=models.CharField(max_length=255)
    small_description=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to="recipe")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="recipe")
    tag=models.ManyToManyField(Tag)
  
    field2=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    def  get_absolute_url(self):
        return reverse_lazy("recipe_detail",kwargs={"pk":self.id})
    
   
    


    








