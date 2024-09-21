from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
