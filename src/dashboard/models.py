from django.db import models
# Create your models here.
from tabnanny import verbose
from django.db import models
from matplotlib.pyplot import title
from django.utils.translation import gettext as _


class showCal(models.Model):
    #id= models.ForeignKey()
    state_no = models.FloatField(_("state_no"), max_length=255)
    crop_name= models.CharField(_("crop_name"), max_length=255)
    yieldd= models.FloatField(_("yield"), max_length=255)
    
    # def __str__(self):
    #     return self.state_no,self.yieldd,self.crop_name
    class Meta:
        verbose_name_plural='ShowCal'
    # def __str__(self):
    #     return self.state_no,self.yieldd,self.crop_name



class Feedback(models.Model):
    #news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    status=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Feedbacks'

    def __str__(self):
        return self.subject


