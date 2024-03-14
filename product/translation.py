from modeltranslation.translator import translator, TranslationOptions
from .models import Recipe

class RecipeTranslationOptions(TranslationOptions):
    fields = ('title',"description"
              )
    
translator.register(Recipe, RecipeTranslationOptions)