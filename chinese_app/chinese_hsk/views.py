from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chinese_hsk/index.html")
def excercises(request):
    return render(request, "chinese_hsk/excercises.html")
