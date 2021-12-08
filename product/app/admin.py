from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import *


admin.site.register(Category)
# admin.site.register(SubCategory)
admin.site.register(Product)
