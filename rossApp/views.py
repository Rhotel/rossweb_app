from django.shortcuts import render
# from http.client import HttpResponse
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello Ross. You are now online!")