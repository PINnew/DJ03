# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'news/index.html')