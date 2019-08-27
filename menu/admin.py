from django.contrib import admin
from .models import Category, Dish 
from parler.admin import TranslatableAdmin


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    """
    """
    list_display        = ["name", "slug"]
    
    #
    def get_prepopulated_fields(self, request, obj = None):
        return {"slug":("name",)}

@admin.register(Dish)
class DishAdmin(TranslatableAdmin):
    """
    """
    list_display        = ["name", "slug", "price"]
    
    #
    def get_prepopulated_fields(self, request, obj = None):
        return {"slug": ("name",)} 

