from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# вьюхи вьюс контроллеры
# Create your views here.

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news,
               'title': 'news list',
               'categories': categories
               }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {'news': news, 'categories': categories, 'category': category}
    return render(request, template_name='news/category.html', context=context)


def test(request):
    news = News.objects.all()
    return render(request, 'news/test.html', {'news': news, 'title': 'test page'})


def published(request):
    news = News.objects.filter(is_published=True)
    context = {'news': news, 'title': 'published news'}
    return HttpResponse(request, 'news/info.html', context)


def info_unpublished(request):
    news = News.objects.filter(is_published=False)
    return HttpResponse(request, 'news/unpublished.html', {'news': news, 'title': 'unpublished news'})
