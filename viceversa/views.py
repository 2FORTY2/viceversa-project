from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'name': 'Vice Versa'})
def reverse(request):
	return render(request, 'reverse.html')