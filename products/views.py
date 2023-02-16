from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, ProductImages

# Create your views here.

class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                                #gets the details of the product
        my_product= self.get_object()                                                               # gets the id for the product
        context["images"] = ProductImages.objects.filter(product=my_product)                        #get the images too
        context["related"] = Product.objects.filter(category=my_product.category)
        return context
    