from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from  django.db.models.aggregates import Avg


PRODUCT_FLAG= (
    ('New', 'New'),
    ('Sale', 'Sale'),
    ('Feature', 'Feature')

)


# model manager
class ProductManager(models.Manager):
    def price_greater_than(self, price):
        return self.filter(price__gt=price)

class Product(models.Model):
    name =models.CharField(_("Name"), max_length=100)
    sku= models.IntegerField(_("SKU"))
    subtitle= models.CharField(_("Subtitle"), max_length=300)
    desc=models.TextField(_("Description"), max_length=10000)
    flag=models.CharField(_("Flag"), max_length=10, choices=PRODUCT_FLAG)
    price= models.FloatField(_("Price"))
    image=models.ImageField(_("Image"), upload_to='products')
    tags= TaggableManager()
    category = models.ForeignKey( 'Category', related_name='product_category', verbose_name=_('Category'), on_delete=models.SET_NULL , null=True, blank=True )
    brand= models.ForeignKey( "Brand", related_name='product_brand',verbose_name=_('Brand'), on_delete=models.SET_NULL, null=True,blank=True)
    video_url= models.URLField(null=True, blank=True)
    quantity = models.IntegerField(_("Quantity"), default=50)

    
    objects = ProductManager()
    
    def __str__(self):
        return self.name

    # average for reviews
    def get_avg(self):
        avg= self.product_review.aggregate(myavg= Avg('rate'))
        return avg

    # another way
    def get_avg2(self):
        rate_sum = 0
        product_review= self.product_review.all()
        for review in product_review :
            rate_sum+= review.rate

        avg= rate_sum / len(product_review)
        return avg


class ProductImages(models.Model):
    product = models.ForeignKey("Product", verbose_name=_("Product"), related_name='product_image', on_delete=models.SET_NULL, null=True, blank=True)
    image=models.ImageField(_("Image"), upload_to='productimages')

    def __str__(self):
        return str(self.product)


class ProductReview(models.Model):
    user=models.ForeignKey(User, verbose_name=_(""),related_name='user_review', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey("Product", verbose_name=_("Product"),related_name='product_review', on_delete=models.SET_NULL, null=True, blank=True)
    rate= models.IntegerField(_("Rate"))
    review= models.CharField(_("Review"), max_length=300)
    created_at = models.DateTimeField(_("Created_at"), default=timezone.now)

    def __str__(self):
        return str(self.product)




class Category(models.Model):
    name=models.CharField( _('Name') , max_length=100,)
    image=models.ImageField(_('Image'),upload_to='category')
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name=models.CharField(_('Name'), max_length=100)
    image=models.ImageField(_('Image'), upload_to='brand')

    def __str__(self):
        return self.name
