from django.urls import  path
from .views import StoreBaseView


urlpatterns=[
    path('',StoreBaseView.as_view(),name='store')
]