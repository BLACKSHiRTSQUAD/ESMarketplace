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
    path('store/<int:es_id>', views.view_store_es, name='store_es'),
    path('store/charge>', views.charge, name='charge'),
    path('get_question_store/<int:q_id>', views.get_question_store, name='purchased'),
    path('purchased/', views.purchased, name='purchased'),
    path('purchased/<int:es_id>', views.view_purchased_es, name='purchased_es'),
    path('get_question_purchased/<int:q_id>', views.get_question_purchased, name='purchased'),
    path('account/', views.account, name='account'),
    path('test/', views.test, name='test'),
    path('testtwo/', views.testtwo, name='testtwo'),
    path('get_question/<int:q_id>/', views.get_question, name='get_question'),
    path('create/edit/<int:es_id>/', views.edit, name='edit'),
    path('create/edit/save_question/<int:q_id>/', views.save_question, name='save_question'),
    path('create/edit/delete_choice/', views.del_choice, name='del_choice'),


]