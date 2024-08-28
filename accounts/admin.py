from django.contrib import admin
from .models import User


@admin.register(User)
class user_account(admin.ModelAdmin):
    pass
