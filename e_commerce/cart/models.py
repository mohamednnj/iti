from django.db import models
from product.models import Product
from accounts.models import User,Product
# Create your models here.
class Cart(models.Model):
    customr = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    selected_product = models.ManyToManyField(Product)