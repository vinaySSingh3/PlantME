"""mapping3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from dashboard import views as DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('newsapp.urls')),
    

    path('', DashboardView.index, name='index'),
    #path('',DashboardView.topfive, name= 'index'),

    #path('about-us', news_views.aboutUs, name='aboutUs'),

    

    #path('', news_views.news, name='index'),
    # path('news',news_views.news, name= 'news'),
    # path('all-news',news_views.all_news, name= 'all-news'),
    # #path('detail/<int:id>',news_views.detail,name='detail'),
    # path('all-category',news_views.all_category, name='all-category'),
    # path('Fungicides', news_views.Fungicides, name='Fungicides'),
    # path('Herbicides', news_views.Herbicides, name='Herbicides'),
    # path('Insecticides', news_views.Insecticides, name='Insecticides'),
    # path('Mothballs', news_views.Mothballs, name='Mothballs'),
    # path('category/<int:id>',news_views.category,name='category'),
    # path('Crop', news_views.Crop, name='Crop'),
    # path('contact-us', news_views.contactUs, name='contactUs'),
    #path('Getnews', include('newsapp.urls')),
    #path('news', include('newsapp.urls'))
    

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)