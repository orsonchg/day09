from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,'app01/index.html')

def alarm(request):
	return render(request, 'alarm.html')