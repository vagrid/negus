
from django.shortcuts import render, get_object_or_404
from .models import Category, Dish

"""
To display the menu, a view is created to 
list all dishes or filter dishes by a given category
"""

#
def dish_list(request, category_slug = None):
    """
    """
    category    = None
    # List of all the categories (available in the database)
    categories  = Category.objects.all() 
    # List of all the dishes (available in the database) 
    dishes      = Dish.objects.all() 
    # 
    if category_slug:
        #
        category    = get_object_or_404(Category, slug = category_slug)
        #
        dishes      = dishes.filter(category = category)
    #
    template_name   = "menu/dish/list.html" 
    #
    context         = {"category":category, "categories":categories, "dishes":dishes} 
    #
    return render(request, template_name, context)
