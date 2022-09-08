from django.http import HttpResponse
from django.http import JsonResponse

def homepage(request):
  return HttpResponse('homepage')

def about(request):
  return HttpResponse('about')

def api(request):
  return JsonResponse({
    "Json": "This is Json data."
  })