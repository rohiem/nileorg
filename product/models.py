from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse







class Product(models.Model):
    name          =models.CharField( max_length=50,verbose_name=_("product name"))
    prdcategory   =models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("category"))
    prdbrand      =models.ForeignKey('settings.Brand',  on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("brand"))
    desc          =models.TextField(verbose_name=_("product description") )
    ProductImage  =models.ImageField( upload_to="product/",verbose_name=_("image"),blank=True,null=True) 
    price         =models.DecimalField(verbose_name=_("price"), max_digits=7, decimal_places=2)
    discount      =models.DecimalField(verbose_name=_("discount"), max_digits=7, decimal_places=2)
    cost          =models.DecimalField(verbose_name=_("cost"), max_digits=7, decimal_places=2)
    created       =models.DateTimeField(verbose_name=_("created at"), auto_now=False, auto_now_add=False)
    slug          =models.SlugField(blank=True ,null=True,verbose_name=_("product url"))
    new           =models.BooleanField(default=True,verbose_name=_("new product"))
    bestseller    =models.BooleanField(default=False,verbose_name=_("bestselletr"))

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Product,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"slug": self.slug})


    


class ProductImage(models.Model):
    Product =models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("product"))
    ProductImage=models.ImageField( upload_to="product/",verbose_name=_("image"))

    def __str__(self):
        return str(self.Product)

class Category(models.Model):
    Product =models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("product category"),blank=True,null=True )
    categoryname=models.CharField(max_length=50,verbose_name=_("category name"))
    categoryparent=models.ForeignKey("self",limit_choices_to={"categoryparent__isnull":True} ,on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("categorty parent"))
    categoryimg=models.ImageField( upload_to="category/",verbose_name=_("category img"))
    categorydesc=models.TextField(verbose_name=_("category desc"))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.categoryname

class Product_Alternative(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name="mainproduct",verbose_name=_("product"))
    prodAlternatives=models.ManyToManyField(Product,related_name="alternativeproducts",verbose_name=_("product alters"))

    class Meta:
        verbose_name =_( 'Product Alternative')
        verbose_name_plural =_('Product Alternatives')  

    def __str__(self):
        return str(self.product)

class Product_Accessories(models.Model):
    productac=models.ForeignKey(Product, on_delete=models.CASCADE,related_name="mainaccproduct",verbose_name=_("product"))
    prodAccessories=models.ManyToManyField(Product,related_name="alternativeaccproducts",verbose_name=_("product accessories"))

    class Meta:
        verbose_name =_('Product accessory') 
        verbose_name_plural =_('Product accessories')  

    def __str__(self):
        return str(self.productac)

