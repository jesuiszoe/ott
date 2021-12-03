from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Netflix
from django.db.models import Q


# Create your views here.
def main(request):
    today = datetime.today().date()
    movies = Netflix.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/main.html', context=context)


# def search(request):
#     movies = Netflix.objects.all().order_by('-id')
#     q = request.POST.get('q','')

#     if q:
#         movies = movies.filter(title__icontains=q)
#         return render(request, 'ott/search.html',{'movies': movies, 'q': q})
#     else:
#         return render(request,'ott/search.html')