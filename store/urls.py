from django.urls import  path
from .views import *


urlpatterns=[
    path('',StoreBaseView.as_view(),name='store'),
    path('<slug:category_slug>/',StoreBaseView.as_view(),name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name="product_detail"),
]
