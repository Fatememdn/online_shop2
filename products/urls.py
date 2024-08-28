from  django.urls import path
from .views import *

urlpatterns= [
    path('list',product_list),
    path('search/name/<str:name>', search_product_by_name),
    path('search/category/<str:category>', search_product_by_category ),
    path('add', add_product),
]