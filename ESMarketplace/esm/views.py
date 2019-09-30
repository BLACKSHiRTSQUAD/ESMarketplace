from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

from .models import ESQuestion, ExpertSystem

# Create your views here.
def home(request):
    context = {'nbar': 'home'}
    return render(request, 'esm/home.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect(reverse('esm:home'))
        else:
            return render(request, 'esm/login.html', {})
    return render(request, 'esm/login.html', {})


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
    context = {'nbar': 'create'}
    return render(request, 'esm/create.html', context)


def edit(request, es_id):

    context = {'nbar': 'account', 'es_id': es_id}
    return render(request, 'esm/edit.html', context)


def store(request):
    context = {'nbar': 'store'}
    return render(request, 'esm/edit.html', context)


def purchased(request):
    context = {'nbar': 'purchased'}
    return render(request, 'esm/purchased.html', context)


def account(request):
    context = {'nbar': 'account'}
    return render(request, 'esm/account.html', context)


def test(request):
    user = User.objects.get(username='juser')
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email

    context = {'nbar': 'test', 'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email}
    return render(request, 'esm/test.html', context)

def get_question(request):
    question = ESQuestion.objects.get(pk=6)
    choice_set = question.esquestion_set.all()

    context = {'nbar': 'test', 'question': question, 'choice_set': choice_set}
    return render(request, 'esm/get_question.html', context)