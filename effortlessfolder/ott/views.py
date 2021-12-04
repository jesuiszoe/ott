from django.shortcuts import render

from datetime import datetime
from .models import Amazon, Disney, Hulu, Netflix
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.


   


def main(request):
    today = datetime.today().date()
    movies = Netflix.objects.all()
    
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    
    
    # 조회
    movies = Netflix.objects.order_by('id')
    kw = request.GET.get('kw','')
    

    # 페이징처리
    paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    
    
    

    
    if 'kw': # 만약 검색어가 존재하면
        movies = movies.filter(title__icontains= kw) # 해당 검색어를 포함한 queryset 가져오기
        paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        
        


    context = {'date': today, 'movies': page_obj , 'page': page ,'kw':kw }

    return render(request, 'ott/main.html', context)

def amazon(request):
    today = datetime.today().date()
    movies = Amazon.objects.all()
    
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    
    
    # 조회
    movies = Amazon.objects.order_by('id')
    kw = request.GET.get('kw','')
    

    # 페이징처리
    paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    
    
    

    
    if 'kw': # 만약 검색어가 존재하면
        movies = movies.filter(title__icontains= kw) # 해당 검색어를 포함한 queryset 가져오기
        paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        
        


    context = {'date': today, 'movies': page_obj , 'page': page ,'kw':kw }

    return render(request, 'ott/amazon.html', context)
    


def hulu(request):
    today = datetime.today().date()
    movies = Hulu.objects.all()
    
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    
    
    # 조회
    movies = Hulu.objects.order_by('id')
    kw = request.GET.get('kw','')
    

    # 페이징처리
    paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    
    
    

    
    if 'kw': # 만약 검색어가 존재하면
        movies = movies.filter(title__icontains= kw) # 해당 검색어를 포함한 queryset 가져오기
        paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        
        


    context = {'date': today, 'movies': page_obj , 'page': page ,'kw':kw }

    return render(request, 'ott/hulu.html', context)

def disney(request):
    today = datetime.today().date()
    movies = Disney.objects.all()
    
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    
    
    # 조회
    movies = Disney.objects.order_by('id')
    kw = request.GET.get('kw','')
    

    # 페이징처리
    paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    
    
    

    
    if 'kw': # 만약 검색어가 존재하면
        movies = movies.filter(title__icontains= kw) # 해당 검색어를 포함한 queryset 가져오기
        paginator = Paginator(movies, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        
        


    context = {'date': today, 'movies': page_obj , 'page': page ,'kw':kw }

    return render(request, 'ott/disney.html', context)
    


def netflix(request):
    today = datetime.today().date()
    movies = Netflix.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/netflix.html', context=context)
