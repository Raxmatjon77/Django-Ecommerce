from django.urls import path
from .views import *
urlpatterns=[
    path('',cart,name='cart'),
    path('add_product/<int:product_id>/', add_cart, name="cart_add")

]