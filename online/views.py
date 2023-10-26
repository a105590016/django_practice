from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello')

def index2(request):
    return render(request, 'index2.html')
