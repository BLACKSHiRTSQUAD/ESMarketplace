from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from .models import ESQuestion, ExpertSystem

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {'nbar': 'home'}
        return render(request, 'esm/home.html', context)
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
        else:
            return render(request, 'esm/login.html', {})
    return render(request, 'esm/login.html', {})


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
        print(user)
        return HttpResponseRedirect(reverse('esm:login'))
    return render(request, 'esm/signup.html', {})


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        cost = request.POST['cost']
        es = ExpertSystem(title=title, cost=cost, owner=request.user)
        es.save()
        q = ESQuestion(es_id=es, qa_text='question title - edit this')
        q.save()
        return HttpResponseRedirect(reverse('esm:edit', kwargs={'es_id': es.pk}))
    esystems = ExpertSystem.objects.all()
    context = {'nbar': 'create', 'esystems': esystems}
    return render(request, 'esm/create.html', context)


def edit(request, es_id):
    es = ExpertSystem.objects.get(pk=es_id)
    q = ESQuestion.objects.get(es_id=es)
    context = {'nbar': 'create', 'es': es, 'question': q}
    return render(request, 'esm/edit.html', context)


def save_question(request, q_id):
    assert request.method == 'POST'
    post_data = request.POST.getlist('data[]')

    q = ESQuestion.objects.get(id=q_id)
    choices = q.esquestion_set.all()
    for i in range(len(choices)):
        if choices[i].prev_choice_text != post_data[i]:
            choice = choices[i]
            choice.prev_choice_text = post_data[i]
            choice.save()
    context = {'nbar': 'create', 'question': q}
    return HttpResponse(status=200)


def store(request):
    context = {'nbar': 'store'}
    return render(request, 'esm/edit.html', context)


def purchased(request):
    context = {'nbar': 'purchased'}
    return render(request, 'esm/purchased.html', context)


def account(request):
    user = request.user
    context = {'nbar': 'account', 'user': user}
    if request.method == 'POST':
        user.username = request.POST['username']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.save()
    return render(request, 'esm/account.html', context)


def test(request):
    user = User.objects.get(username='juser')
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email

    context = {'nbar': 'test', 'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email}
    return render(request, 'esm/test.html', context)


def get_question(request, q_id):
    question = ESQuestion.objects.get(pk=q_id)
    choice_set = question.esquestion_set.all()

    context = {'nbar': 'test', 'question': question, 'choice_set': choice_set}
    return render(request, 'esm/get_question_edit.html', context)