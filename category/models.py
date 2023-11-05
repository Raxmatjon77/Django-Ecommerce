from django.db import models
from django.urls import  reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    description=models.TextField(blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    image=models.ImageField(blank=True,upload_to='photo/category')

    def __str__(self):
        return  self.name

    def get_url(self):
        return  reverse('product_by_category',args=[self.slug])