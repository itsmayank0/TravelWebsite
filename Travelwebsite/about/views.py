from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def team(request):
    return HttpResponse(render(request, 'about.html', {'Head' : 'Mayank'}))
