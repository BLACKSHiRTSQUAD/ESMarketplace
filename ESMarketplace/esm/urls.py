from django.urls import path, re_path

from . import views

app_name = 'esm'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('purchased/', views.purchased, name='purchased'),
    path('purchased/<int:es_id>', views.view_purchased_es, name='purchased'),
    path('get_question_purchased/<int:q_id>', views.get_question_purchased, name='purchased'),
    path('account/', views.account, name='account'),
    path('test/', views.test, name='test'),
    path('get_question/<int:q_id>/', views.get_question, name='get_question'),
    path('create/edit/<int:es_id>/', views.edit, name='edit'),
    path('create/edit/save_question/<int:q_id>/', views.save_question, name='save_question'),


]