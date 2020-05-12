from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main_page/index.html')


def about(request):
    return render(request, 'main_page/about.html')


def services(request):
    return render(request, 'main_page/services.html')
