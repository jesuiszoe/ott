from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Netflix

# Create your views here.
def main(request):
    today = datetime.today().date()
    movies = Netflix.objects.all()
    context = {'date':today,'movies' :movies}
    
    return render(request, 'ott/main.html', context=context)