from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.


def login(request):
    # template = loader.get_template('login/index.html')
    # context = {}
    return render(request,'login/index.html')

