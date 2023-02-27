from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product, ProductImages , Brand , Category
from  django.db.models import Count , Q , F, Value
from  django.db.models.functions import Concat
from  django.db.models.aggregates import Min,Max,Sum

# Create your views here.

def post_list(request):
    # objects=Product.objects.all()
    # price__gt , price__gte , price__lt , price__range(n,n)
    # objects=Product.objects.filter(price__lt=30)
    # category__id , category__id__gt
    # objects=Product.objects.filter(category__id=10) 
    # name__contains , name__startswith , name__endswith 
    # desc__innull = True -> checks if column has no description
    # objects=Product.objects.filter(name__contains="Sarah")
    # objects=Product.objects.filter( quantity__gt=10, price__gt=50 )  # this is and
    # objects=Product.objects.filter( Q(quantity__gt=10) & Q(price__gt=50) ) # this is and
    #  & ~ means AND NOT
    # objects=Product.objects.filter( Q(quantity__gt=10) | Q(price__gt=50)  ) # this is or
    # objects=Product.objects.filter( quantity= F('price') ) # to compare 2 cols
    # objects=Product.objects.order_by('name' , '-price') # to compare 2 cols
    # objects=Product.objects.filter(Q(quantity__gt=50) | Q(price__gt=50)).order_by('name') 
    # objects=Product.objects.values_list('id' , 'price ')  # this brings only specific columns from db in dic
    # objects=Product.objects.only('id' , 'name') #-> takes too much time
    # use select_related for getting query from a related column ( one to one , foreign key )
    # objects=Product.objects.select_related("category").all() 
    #objects=Product.objects.prefetch_related("category").all() # the same but (many to many)
    # objects=Product.objects.annotate(is_new=Value(True)) # to make a new column 
    # if u want to make a new column that consist of two column
    # objects=Product.objects.annotate(
    #     Name_Flag= Concat('name', Value(' -> '), 'flag')

    # ) 
    objects=Product.objects.aggregate(Sum('price'), Max('price'))

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