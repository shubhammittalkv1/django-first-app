from django.shortcuts import render
from django.Http import HttpResponse

def home(request):
   		return HttpResponse('hey this is shubham', content_type='text/html')
