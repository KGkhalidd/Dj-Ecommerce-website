from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, ProductImages , Brand , Category
from  django.db.models import Count

# Create your views here.

def post_list(request):
    objects=Product.objects.all()
    return render(request , 'products/test_list.html',{'products':objects} )


class ProductList(ListView):
    model = Product
    paginate_by= 100


class ProductDetail(DetailView):
    model = Product

    # for edit , delete , detail -> use get_object
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                                #gets the details of the product
        my_product= self.get_object()                                                               # gets the id for the product
        context["images"] = ProductImages.objects.filter(product=my_product)                        #get the images too
        context["related"] = Product.objects.filter(category=my_product.category)
        return context
    

class BrandList(ListView):
    model= Brand
    #paginate_by= 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                                #gets the details of the product
        context['brands'] = Brand.objects.all().annotate(product_count= Count('product_brand'))
        return context

    '''
    brand table

    id     name   image  product_count
    1      apple    ''     the relation between the brand & product
    
    '''

class BrandDetail(DetailView):
    model = Brand

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_brand= self.get_object()
        context["brand_products"] = Product.objects.filter(brand=my_brand)
        return context
    

class CategoryList(ListView):
    model= Category
    #paginate_by= 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                                #gets the details of the product
        context['category'] = Category.objects.all().annotate(product_count= Count('product_category'))
        return context