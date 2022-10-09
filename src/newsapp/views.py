from django.http import HttpResponse
from django.shortcuts import render
from .models import News,Category,Comment
from django.contrib import messages
from newsapp.models import News,Category,Comment


# Create your views here.



def news(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[0:3]
    three_categories=Category.objects.all()[0:3]
    return render(request,'news.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html', {
        'all_news':all_news
    })

# Fetch all category
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })


# Fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category,
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted!!!')
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    comments=Comment.objects.filter(news=news,status=True).order_by('-id')
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news,
        'comments':comments
    })


def Fungicides(request):
    return render(request,'Fungicides.html')

def Herbicides(request):
    return render(request,'Herbicides.html')

def Insecticides(request):
    return render(request,'Insecticides.html')

def Mothballs(request):
    return render(request,'Mothballs.html')

def Crop(request):
    return render(request,'Crop.html')

def aboutUs(request):
    return render(request,'about-us.html')

def contactUs(request):
    return render(request,'contact-us.html')

