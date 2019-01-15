from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'login'
# wrong username or password is their it will redirect to login1
urlpatterns = [
    url(r'^check/$', views.check, name='check'),
    url(r'^$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signupcheck/$', views.signupcheck, name='signupcheck'),
]
