from  django.urls import path
from .views import *

urlpatterns= [
    path('add_user', add_user),
    path('user_list', user_list),
    ]