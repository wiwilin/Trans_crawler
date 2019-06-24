from django.shortcuts import render
from django_web.models import ArtiInfo

#from django.core.paginator import Paginator

# Create your views here.
def index(request):

    #limit = 4
    arti_info = ArtiInfo.objects[:1]
    #paginatior = Paginator(arti_info,limit)
    #page = request.get.GET('page',1)
    #load = paginatior.page(page)

    context = {
        'title': arti_info[0].title,
        'des': arti_info[0].des,
        'score':arti_info[0].scores
    }
    return render(request, 'index.html',context)