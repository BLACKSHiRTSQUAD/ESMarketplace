from django.urls import path, re_path

from . import views

app_name = 'esm'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('search/<int:es_id>', views.search_es, name='search_es'),
    path('get_question_search/<int:q_id>', views.search_get_question, name='get_question_search'),
    path('get_question/<int:q_id>/', views.create_get_question, name='get_question'),
    path('create/edit/<int:es_id>/', views.create_edit_es, name='edit'),
    path('create/edit/save_question/<int:q_id>/', views.create_save_question, name='save_question'),
    path('create/edit/delete_choice/', views.create_del_choice, name='del_choice'),
    path('account/', views.account, name='account'),

]