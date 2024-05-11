from django.http import *
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from user.models import User
from .models import *


@validate_user
def redirector(request: HttpRequest):
    if request.method == "GET":
        return redirect('/forum/')
    else:
        raise Http404()


def login(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'auth/login.html')

    elif request.method == "POST":
        try:
            email, password = get_auth_login(request)
            user = User.objects.get(
                email=email,
                password=password
            )
            response = HttpResponseRedirect('/forum/')
            response = set_auth_cookies(response, user)
            return response

        except User.DoesNotExist:
            return render(request, 'auth/login.html', {'error': 'invalid email or password'})
    else:
        raise Http404()


def logout(request: HttpRequest):
    if request.method == "GET":
        response = HttpResponseRedirect('/login/')
        response.delete_cookie('username')
        response.delete_cookie('email')
        response.delete_cookie('login')
        return response
    else:
        raise Http404()


def register(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'auth/register.html')

    elif request.method == "POST":
        try:
            username, email, password = get_auth_register(request)
            user = User.objects.create(
                username=username,
                email=email,
                password=password
            )
            response = HttpResponseRedirect('/forum/')
            response = set_auth_cookies(response, user)
            return response

        except IntegrityError:
            return render(request, 'auth/register.html', {'error': 'username already taken'})

    else:
        raise Http404()


@validate_user
def rules(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'main/rules.html')
    else:
        raise Http404()


@validate_user
def about(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'main/about.html')
    else:
        raise Http404()
