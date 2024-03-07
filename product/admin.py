from django.contrib import admin
from django import forms
from .models import Recipe,Category,Tag,RecipeImages,RecipeReview

admin.site.register([Category,Tag,RecipeImages,RecipeReview])


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=("tag",)
        widgets={
            "tag":forms.CheckboxSelectMultiple()
        }
        


class RecipeImagesInline(admin.TabularInline):
    model=RecipeImages


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    form=RecipeForm
    list_display=("title","category","description",)
    list_display_links=("description","title",)
    list_filter=("category",)
    search_fields=("title","category__title")
    list_editable=("category",)
    # list_per_page=1
    inlines=[RecipeImagesInline]
    fieldsets=((
        "Information",{
            "fields":("title","description","image",)
        }
    ),
    (
        "Related Fields",{
            "fields":("user","category","tag")
        }

    ),
   
    )











  


    






    
    


   