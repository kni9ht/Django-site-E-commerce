from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def save(request):
    uname = request.POST['user']
    uemail = request.POST['email']
    upasswd = request.POST['password']
    unumber = request.POST['number']
    bot = User.objects.create_user(uname, uemail, upasswd)
    bot.save()
    return redirect('/login')


def login_useer(request):
    if request.method == "POST":
        user = auth.authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.warning(request, 'Invalid credential,Try again')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404("access denied")

    return redirect(request.META['HTTP_REFERER'])


def logout_user(request):
    logout(request)
    return redirect('/home')
