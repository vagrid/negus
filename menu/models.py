from django.db import models
from parler.models import TranslatableModel, TranslatedFields

"""
The menu of the negus restaurant consists of dishes that are 
organized into different categories.
Each dish has a name, discription, prince, etc. 

Two models: Category and Dish 
- Category
    + name field
    + slug unique field (implies the creation of an index)
- Dish 
    + category ForeignKey (many-to-one relationship, which means a dish belongs to one category only, but a category contains  multiple dishes)
    + name 
    + slug 
    + description
    + price 
"""
# 
class Category(TranslatableModel):
    """
    """
    translations = TranslatedFields(
        name     = models.CharField(max_length = 200, db_index = True),
        slug     = models.SlugField(max_length = 200, db_index = True, unique = True) 
    )
    position    = models.PositiveIntegerField(unique = True)
    #
    class Meta:
        """
        """
        ordering            = ("position",)
        verbose_name        = "category"
        verbose_name_plural = "categories"
   
    #
    def __str__(self):
        """
        """ 
        return self.name 


#
class Dish(TranslatableModel):
    """
    """
    translations    = TranslatedFields(
        name        = models.CharField(max_length = 200, db_index = True),
        slug        = models.SlugField(max_length = 200, db_index = True), 
        description = models.TextField(blank = True)
    )
    category = models.ForeignKey(Category, related_name = "dishes", on_delete = models.CASCADE)
    price       = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    #
    #class Meta:
    #    """
    #    """
        #ordering        = ("name", )
        #index_together  = (("id", "slug"),)
    
    #
    def __str__(self):
        """
        """
        return self.name 


