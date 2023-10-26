from django.shortcuts import render
from django.views import View

from store.models import Product


# Create your views here.
class StoreBaseView(View):
     def get(self,request):
         products=Product.objects.filter(is_available=True)
         product_count=Product.objects.count()
         context={
             'products':products,
             'product_count':product_count
         }

         return  render(request,'store.html',context)