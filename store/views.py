from django.shortcuts import render, get_object_or_404
from django.views import View

from category.models import Category
from store.models import Product


# Create your views here.
class StoreBaseView(View):
    def get(self,request,category_slug=None):

        product_count = Product.objects.count()
        products=Product.objects.filter(is_available=True)
        if category_slug is not  None:
            category=get_object_or_404(Category,slug=category_slug)
            products=Product.objects.filter(is_available=True,category=category)
            product_count = products.count()
        context={
             'products':products,
             'product_count':product_count
                }


        return  render(request,'store.html',context)
def product_detail(request,category_slug,product_slug):
        product=get_object_or_404(Product,slug=product_slug,category__slug=category_slug)
        context={
            'product':product
        }
        return render(request,'product_detail.html',context)
