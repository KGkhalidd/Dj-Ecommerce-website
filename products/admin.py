from django.contrib import admin
from .models import Product , ProductImages , ProductReview , Category , Brand
# Register your models here.


class ProductImagesInlines(admin.TabularInline):
    model= ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'price']
    inlines= [ProductImagesInlines]

admin.site.register(Product,ProductAdmin )
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Category)
admin.site.register(Brand)