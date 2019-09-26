from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
        user = User.objects.create_user(username, email, password,first_name=firstname, last_name=lastname)
        user.save()
        print(user)
        return HttpResponseRedirect(reverse('esm:login'))
    return render(request, 'esm/signup.html', {})


def create(request):
    context = {'nbar': 'create'}
    return render(request, 'esm/create.html', context)


def store(request):
    context = {'nbar': 'store'}
    return render(request, 'esm/store.html', context)


def purchased(request):
    context = {'nbar': 'purchased'}
    return render(request, 'esm/purchased.html', context)


def account(request):
    context = {'nbar': 'account'}
    return render(request, 'esm/account.html', context)
