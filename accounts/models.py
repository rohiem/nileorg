from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.db.models.signals import pre_init 
from django.db.models.signals import pre_save ,post_save

class Profile(models.Model):
    user=models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    slug=models.SlugField(blank=True,null=False)
    address=models.CharField( max_length=50)
    joindate=models.DateTimeField(_("join date"),default=datetime.datetime.now)
    country=CountryField()
    image=models.ImageField(_("image"), upload_to="profile_img",blank=True,null=True)


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

  #  def get_absolute_url(self):
     #   return reverse("accounts:profile", kwargs={"slug": self.slug})
    #

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])




post_save.connect(create_profile,sender=User)