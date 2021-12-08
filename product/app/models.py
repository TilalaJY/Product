from django.db import models
from django.db.models.fields import IntegerField
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

# Create your models here.

# class Category(models.Model):
#     category = models.CharField(max_length=100)
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)

class Category(models.Model):
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.category +"_"+self.sub_category

class Product(models.Model):
    Name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=10)
    price = models.IntegerField()
    category = models.ForeignKey('Category', related_name='Product', on_delete=models.CASCADE, blank=True, null=True)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Product', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.Name
