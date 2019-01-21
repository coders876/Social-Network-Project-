from . import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'login'
# wrong username or password is their it will redirect to login1
urlpatterns = [

    path('', views.login, name='login'),
    path('signup/', views.UserFormView.as_view(), name='register'),
    path('check/', views.check, name='check'),
    #path('signupcheck/', views.signupcheck, name='signupcheck'),
    path('home/', views.home, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


