from django.urls import path, re_path

from . import views

app_name = 'marketplaceApp'
urlpatterns = [
    path('', views.MainPageView.as_view(), name='index'),

]