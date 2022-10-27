from django.shortcuts import render
from .models import (
    AboutAreas,
    News
)

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def test(request):
    return render(request, 'index.htm')

def testPk(request):
    return render(request, 'pages/template.htm')

def testAll(request):
    return render(request, 'pages/templateall.htm')

def NewsOne(request, slug):
    """ Bitta yangilikni ko'rsatadi """
    news = News.objects.get(slug=slug)
    return render(request, 'onepages/newsone.htm', context={
        'news':news,
    })

class NewsList(ListView):
    """ Hamma Yangiliklarni ko'rsatadi """
    model= News
    ordering = '-add_time'
    template_name = 'allpages/news.htm'

class AreasDetail(DetailView):
    """ Hamma hududlarni ko'rsatadi """
    model = AboutAreas
    template_name = 'onepages/areasone.htm'

class AreasList(ListView):
    """ Hamma hududlarni ko'rsatadi """
    model = AboutAreas
    ordering = 'uz_title'
    template_name = 'allpages/areas.htm'

