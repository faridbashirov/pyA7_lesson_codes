from django.contrib import admin
from django import forms
from .models import Recipe,Category,Tag,RecipeImages
admin.site.register([Category,Tag])


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=("tag",)
        widgets={
            "tag":forms.CheckboxSelectMultiple
        }
class RecipeImagesInline(admin.TabularInline):
    model=RecipeImages

@admin.register(Recipe)
class RecipAdmin(admin.ModelAdmin):
    form=RecipeForm
    inlines=[RecipeImagesInline]
    list_display=["title","description","category"]
    list_display_links=("title","description",)
    list_editable=("category",)
    list_filter=("category",)
    search_fields=("title",)
    prepopulated_fields={
        "slug":("title",)
    }
    fieldsets=((
        "Information",{
            "fields":("title","description","image","slug","user",)
            
        }
    ),
    ("Related Fields",{
        "fields":("tag","category",)
    })
    )


    






    
    


   