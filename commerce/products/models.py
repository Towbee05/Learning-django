from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120, blank=False, null = False)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100000)
    category = models.ForeignKey(Category, on_delete =models.CASCADE)
    description = models.CharField(max_length= 10000000)
    price = models.DecimalField(decimal_places = 2, max_digits= 10000)
    added_to_cart = models.BooleanField(default=False)
    in_sales = models.BooleanField(default=True)
    image = models.ImageField(blank = False, null=False, upload_to="images/")

    def __str__(self):
        return self.name



    def get_absolute_url(self):
        return reverse ("details", kwargs={"id" : self.id})
    
    def get_absolute_url_2(self):
        return reverse ("edit", kwargs={"id" : self.id})