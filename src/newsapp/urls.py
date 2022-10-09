
from tokenize import Name
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_view

from . import views


 
urlpatterns = [
    path('all-news',views.all_news,name='all-news'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),

    path('news', views.news, name='news'),
    
    path('Fungicides', views.Fungicides, name='Fungicides'),
    path('Herbicides', views.Herbicides, name='Herbicides'),
    path('Insecticides', views.Insecticides, name='Insecticides'),
    path('Mothballs', views.Mothballs, name='Mothballs'),
    path('Crop', views.Crop, name='Crop'),
    
    
    path('about-us',views.aboutUs,name='aboutUs'),
    path('contact-us',dashboard_view.contact,name='contact-us'),

    #path('', dashboard_view.index, name='index'),
    
    
    




    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)