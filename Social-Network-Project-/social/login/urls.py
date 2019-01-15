from . import views
from django.urls import path
from django.conf.urls import url,include


from django.conf.urls import url

urlpatterns = [
    path('', views.login , name='login')
]
