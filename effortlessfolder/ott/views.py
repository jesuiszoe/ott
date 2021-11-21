from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def main(request):
    today = datetime.today().date()
    context = {'date':today,}
    return render(request, 'ott/main.html', context=context)