from django.contrib import admin
from django import forms
from .models import Recipe,Category,Tag,RecipeImages,RecipeReview

admin.site.register([Category,Tag,RecipeImages,RecipeReview,Recipe])


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=("tag",)
        widgets={
            "tag":forms.CheckboxSelectMultiple()
        }
        


class RecipeImagesInline(admin.TabularInline):
    model=RecipeImages













  


    






    
    


   