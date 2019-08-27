from django.contrib import admin
from .models import Category, Dish 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    """
    list_display        = ["name", "slug"]
    prepopulated_fields = {"slug":("name",)}

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """
    """
    list_display        = ["name", "slug", "price"]
    prepopulated_fields = {"slug": ("name",)} 

