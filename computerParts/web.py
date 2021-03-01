from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, AnonymousUser
from login.models import product


def home(request):
    user = request.user
    userauth = user.is_authenticated
    useran = user.is_anonymous
    print(user.username)
    return render(request, 'index.html', {'user': user, 'userauth': userauth, 'useran': useran})


def desktop(request):
    data = {'dataset': product.objects.filter(product_type="desktop")}
    return render(request, 'desktop.html', data)


def accessory(request):
    data = {'dataset': product.objects.filter(product_type="accessory")}
    return render(request, 'accessory.html', data)


def laptop(request):
    data = {'dataset': product.objects.filter(product_type="laptop")}
    return render(request, 'laptop.html', data)


def logout_user(request):
    auth.logout(request)
    return redirect(request.META['HTTP_REFERER'])
