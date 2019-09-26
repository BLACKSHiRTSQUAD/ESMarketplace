from django.urls import path, re_path

from . import views

app_name = 'esm'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]