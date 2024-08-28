from django.contrib import admin
from .models import *



@admin.register(Category)
class cat(admin.ModelAdmin):
    pass




@admin.register(Product)
class pro(admin.ModelAdmin):
    pass