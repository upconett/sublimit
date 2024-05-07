from django.http import *
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from user.models import User, Article


def redirector(request: HttpRequest):
    if request.method == "GET":
        try:
            email, username, password = get_auth_cookies(request)
            User.objects.get(
                email=email, 
                username=username, 
                password=password
                )
            return redirect('/home/')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')

    else:
        return Http404()


def home(request: HttpRequest):
    if request.method == "GET":
        pass

    else:
        return Http404()


def login(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'auth/login.html')

    elif request.method == "POST":
        pass

    else:
        return Http404()


def register(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'auth/register.html')

    elif request.method == "POST":
        pass

    else:
        return Http404()