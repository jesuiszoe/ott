from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Amazon, Disney, Hulu, Netflix
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


def main(request):
    today = datetime.today().date()
    movies = Netflix.objects.all()
    """
    pybo 목록출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    movies = Netflix.objects.order_by('id')
    
    if kw:
        movies = movies.filter(
            Q(title__icontains=kw)   # 제목검색
           
        ).distinct()

    # 페이징처리
    paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'date': today, 'movies': page_obj , 'page': page, 'kw': kw}

    return render(request, 'ott/main.html', context)

def amazon(request):
    today = datetime.today().date()
    movies = Amazon.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/amazon.html', context=context)


def hulu(request):
    today = datetime.today().date()
    movies = Hulu.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/hulu.html', context=context)

def disney(request):
    today = datetime.today().date()
    movies = Disney.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/disney.html', context=context)


def netflix(request):
    today = datetime.today().date()
    movies = Netflix.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/netflix.html', context=context)
