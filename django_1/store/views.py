from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

def product(request):
    return HttpResponse("product page")

def category(request):
    return HttpResponse("category page")

