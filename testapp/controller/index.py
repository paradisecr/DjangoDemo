from django.shortcuts import render
from django.shortcuts import HttpResponse
from testapp import models
# Create your views here.

def test(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'sb_test.html')
