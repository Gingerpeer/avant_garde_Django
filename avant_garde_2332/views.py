from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def homepage(request):
  return render(request,'homepage.html')

def about(request):
  return render(request,'about.html')

def api(request):
  return JsonResponse({
    "Json": "This is Json data."
  })