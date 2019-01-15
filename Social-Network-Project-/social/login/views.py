from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from login.forms import SignUpForm
# Create your views here.


def check(request):
    username1 = request.POST['username1']
    password1 = request.POST['password1']
    user = authenticate(username=username1 , password=password1)
    if user is not None:
        login(request, user)
        return HttpResponse("<h1>you have successfully logged in </h1>")
    else:
        return render(request, 'login/index.html', {})


def login(request):
    return render(request, 'login/index.html', {})


def signupcheck(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return HttpResponse("<h1>you have successfully signed in</h1>")

    return render(request, 'login/signup.html')

def signup(request):
    return render(request, 'login/signup.html',{})