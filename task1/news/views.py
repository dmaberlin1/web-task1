from django.http import HttpResponse
from django.shortcuts import render
from .models import News


# вьюхи вьюс контроллеры
# Create your views here.

def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'news list'}
    return render(request, 'news/index.html', context)


def test(request):
    news = News.objects.all()
    return render(request, 'news/test.html', {'news': news, 'title': 'test page'})


def published(request):
    news = News.objects.filter(is_published=True)
    context={'news': news, 'title': 'published news'}
    return HttpResponse(request, 'news/info.html', context)


def info_unpublished(request):
    news = News.objects.filter(is_published=False)
    return HttpResponse(request, 'news/unpublished.html', {'news': news, 'title': 'unpublished news'})
