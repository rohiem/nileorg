from django.db import models
from accounts.models import Profile
from django.utils.translation import ugettext_lazy as _
from product.models import Product
# Create your models here.
class OrderItem(models.Model):
    product=models.OneToOneField(Product, verbose_name=_("product"), on_delete=models.CASCADE,null=True)
    is_ordered =models.BooleanField(default=False)
    date_added=models.DateTimeField(auto_now=True)
    date_ordered=models.DateTimeField(null=True)




    def __str__(self):
        return self(self.product)
    






class Order(models.Model):
    ref_code       =models.CharField(max_length=15)
    owner          =models.ForeignKey(Profile, verbose_name=_("owner"), on_delete=models.CASCADE)
    is_ordered     =models.BooleanField(default=False)
    items          =models.ManyToManyField(OrderItem, verbose_name=_("item"))
    #payment_detail =models.ForeignKey(Payment, verbose_name=_("payment detail"),null=True)
    date_orderd    =models.DateTimeField( auto_now=True)


    def get_cart_items(self):
        return self.items.all()


    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])


    def __str__(self):
        return str(self.owner)+" - "+str(self.ref_code)