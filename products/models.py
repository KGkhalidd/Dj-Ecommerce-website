from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

PRODUCT_FLAG= (
    ('New', 'New'),
    ('Sale', 'Sale'),
    ('Feature', 'Feature')

)

class Product(models.Model):
    name =models.CharField(_("Name"), max_length=100)
    sku= models.IntegerField(_("SKU"))
    subtitle= models.CharField(_("Subtitle"), max_length=300)
    desc=models.CharField(_("Description"), max_length=10000)
    flag=models.CharField(_("Flag"), max_length=10, choices=PRODUCT_FLAG)
    price= models.FloatField(_("Price"))
    tags= TaggableManager()
    category = models.ForeignKey( 'Category', related_name='product_category', verbose_name=_('Category'), on_delete=models.SET_NULL , null=True, blank=True )
    brand= models.ForeignKey( "Brand", related_name='product_brand',verbose_name=_('Brand'), on_delete=models.SET_NULL, null=True,blank=True)
    video_url= models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey("Product", verbose_name=_("Product"), related_name='productimages_product', on_delete=models.SET_NULL, null=True, blank=True)
    image=models.ImageField(_("Image"), upload_to='productimages')

    def __str__(self):
        return str(self.name)


class ProductReview(models.Model):
    user=models.ForeignKey(User, verbose_name=_(""),related_name='user_review', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey("Product", verbose_name=_("Product"),related_name='product_image', on_delete=models.SET_NULL, null=True, blank=True)
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