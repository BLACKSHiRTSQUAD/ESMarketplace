import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.conf import settings

from .models import *
from .forms import *


#######################################################################################################################
# Account and user
def home(request):
    if request.user.is_authenticated:
        context = {'nbar': 'home', 'path': "esm/home.html"}
        return HttpResponseRedirect(reverse('esm:search'))
    else:
        return HttpResponseRedirect(reverse('esm:login'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('esm:home'))
    return render(request, 'esm/user_login.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('esm:home'))


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
        user.save()
        return HttpResponseRedirect(reverse('esm:login'))
    return render(request, 'esm/user_signup.html', {})


def account(request):
    user = request.user
    if request.method == 'POST':
        u_form = AccountForm(request.POST, instance=user)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = AccountForm(instance=user)
    context = {'nbar': 'account', 'user': user, 'u_form': u_form, 'path': 'esm/user_account.html'}
    return render(request, 'esm/base_html_user.html', context)

#######################################################################################################################
# Create
def create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('esm:login'))
    create_es_form = CreateESForm(request.POST or None)
    if create_es_form.is_valid():
        new_es = create_es_form.save(commit=False)
        new_es.owner = request.user
        new_es.save()
        new_q = ESQuestion(es_id=new_es, qa_text="Initial question goes here.")
        new_q.save()
    esystems = ExpertSystem.objects.all()
    escategories = ESCategoryThree.objects.all()
    context = {'nbar': 'create', 'esystems': esystems, 'create_es_form': create_es_form, 'path': 'esm/create.html',
               'escategories': escategories}
    return render(request, 'esm/base_html_user.html', context)


def create_edit_es(request, es_id):
    es = ExpertSystem.objects.get(pk=es_id)
    q = ESQuestion.objects.get(es_id=es)
    context = {'nbar': 'create', 'es': es, 'question': q, 'path': 'esm/create_edit_es.html'}
    return render(request, 'esm/base_html_user.html', context)


def create_get_question(request, q_id):
    question = ESQuestion.objects.get(pk=q_id)
    choice_set = question.esquestion_set.all()
    context = {'nbar': 'test', 'question': question, 'choice_set': choice_set}
    return render(request, 'esm/create_get_question.html', context)


def create_save_question(request, q_id):
    assert request.method == 'POST'
    post_data = json.loads(json.dumps(request.POST))
    q = ESQuestion.objects.get(id=q_id)
    # if key contains "new", then add to database.
    # if it's a database key, then look for the choice and if different, modify it
    for key, val in post_data.items():
        if key == "question_text":
            if q.qa_text != val:
                q.qa_text = val
                q.save()
        elif "new_" in key:
            ch = ESQuestion(prev_question_id=q, prev_choice_text=val)
            ch.save()
        else:
            ch = ESQuestion.objects.get(pk=key)
            if val != ch.prev_choice_text:
                ch.prev_choice_text = val
                ch.save()

    context = {'nbar': 'create', 'question': q}
    return HttpResponse(status=200)


def create_del_choice(request):
    assert request.method == 'POST'
    post_data = json.loads(json.dumps(request.POST))
    del_key = post_data['delete_id']
    if "new_" in del_key:
        pass
    else:
        get_object_or_404(ESQuestion, pk=del_key).delete()
    return HttpResponse(status=200)

#######################################################################################################################
# Search
def search(request):
    esystems = ExpertSystem.objects.all()
    context = {'nbar': 'search', 'path': 'esm/search.html', 'esystems': esystems}
    return render(request, 'esm/base_html_user.html', context)


def search_es(request, es_id):
    es = ExpertSystem.objects.get(pk=es_id)
    q = ESQuestion.objects.get(es_id=es)
    context = {'nbar': 'search', 'es': es, 'question': q, 'path': 'esm/search_es.html'}
    return render(request, 'esm/base_html_user.html', context)


def search_get_question(request, q_id):
    question = ESQuestion.objects.get(pk=q_id)
    choice_set = question.esquestion_set.all()
    context = {'nbar': 'search', 'question': question, 'choice_set': choice_set}
    return render(request, 'esm/search_get_question.html', context)





