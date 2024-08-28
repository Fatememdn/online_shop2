from  django.urls import path
from .views import *

urlpatterns= [
    path('view/<int:user_id>', view_cart),
    path("add_product_to_cart", add_product_to_cart),
]
