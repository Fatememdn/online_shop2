from django.contrib import admin
from .views import *

class order(admin.TabularInline):
    model = OrderDetail
    extra = 0
    

@admin.register(UserOrder)
class cart(admin.ModelAdmin):
    inlines = [order]