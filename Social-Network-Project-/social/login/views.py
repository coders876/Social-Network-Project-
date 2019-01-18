from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.views import generic
from django.views.generic import View
# Create your views here.


@login_required
def home(request):
    return render(request, 'login/home.html')


def check(request):
    username1 = request.POST['username1']
    password1 = request.POST['password1']
    user = authenticate(username=username1 , password=password1)
    if user is not None:
        auth_login(request, user)
        return redirect('login:home')
    else:
        return render(request, 'login/index.html', {})


def login(request):
    return render(request, 'login/index.html', {})

"""
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

"""
class UserFormView(View):
    form_class = UserRegisterForm
    template_name = 'login/signup.html'

    #display blank form
    def get(self , request):
        form  = self.form_class(None)
        return render(request , self.template_name , {'form':form})

    # process form data
    def post(self , request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1!= password2:
                return render(request , self.template_name , {'form':user})

            user.set_password(password1)
            user.save()

            #return User objects if credentials are correct
            user = authenticate(username = username , password = password1)

            if user is not None:

                if user.is_active:

                    auth_login(request,user)
                    return redirect('login:home')

        return render(request , self.template_name , {'form':form})

















