from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name = 'Categories'

    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=PROTECT, null = True)
    price = models.IntegerField()
    image = models.ImageField()


    def __str__(self):
        return self.name