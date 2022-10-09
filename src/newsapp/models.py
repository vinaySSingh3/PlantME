from tabnanny import verbose
from django.db import models
from matplotlib.pyplot import title
from django.utils.translation import gettext as _

# class showAI(models.Model):
#     #id= models.ForeignKey()
#     state_no = models.FloatField(_("state_no"), max_length=255)
#     crop_name= models.CharField(_("crop_name"), max_length=255)
#     yieldd= models.FloatField(_("yield"), max_length=255)
#     # def __str__(self):
#     #     return self.state_no,self.yieldd,self.crop_name
#     class Meta:
#         verbose_name_plural='ShowAI'



class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

#news model creating here

class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title

#cmt model
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=True)
    

    class Meta:
        verbose_name_plural='Comments'

    def __str__(self):
        return self.comment


