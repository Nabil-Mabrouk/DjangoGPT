

from django.views import View
from django.shortcuts import render

def index(request):
    return render(request, 'landing/index.html')
