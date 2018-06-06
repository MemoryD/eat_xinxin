from django.contrib import admin

# Register your models here.
from .models import Category, School, Food

admin.site.register(Category)
admin.site.register(School)
admin.site.register(Food)