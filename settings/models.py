from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Brand(models.Model):
    BrdName = models.CharField( max_length=50)
    brdDesc =models.TextField(blank=True,null=True)

    def __str__(self):
        return self.BrdName

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Variant(models.Model):
    VarName = models.CharField( max_length=50)
    VarDesc =models.TextField(blank=True,null=True)

    

    class Meta:
        verbose_name = _("variant")
        verbose_name_plural = _("variants")

    def __str__(self):
        return self.VarName






