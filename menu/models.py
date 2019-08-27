from django.db import models


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
class Category(models.Model):
    """
    """
    name        = models.CharField(max_length = 200, db_index = True)
    slug        = models.SlugField(max_length = 200, unique = True) 
    
    #
    class Meta:
        """
        """
        ordering            = ("name",)
        verbose_name        = "category"
        verbose_name_plural = "categories"
   
    #
    def __str__(self):
        """
        """ 
        return self.name 


#
class Dish(models.Model):
    """
    """
    category    = models.ForeignKey(Category, related_name = "dishes", on_delete = models.CASCADE)
    name        = models.CharField(max_length = 200, db_index = True)
    slug        = models.SlugField(max_length = 200, db_index = True) 
    description = models.TextField(blank = True)
    price       = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    #
    class Meta:
        """
        """
        ordering        = ("name", )
        index_together  = (("id", "slug"),)
    
    #
    def __str__(self):
        """
        """
        return self.name 


