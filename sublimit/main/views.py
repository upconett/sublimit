from django.http import *
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from user.models import User
from .models import *


def redirector(request: HttpRequest):
    if request.method == "GET":
        try:
            validate_user(request)
            return redirect('/home/')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')

    else:
        return Http404()


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
            response = HttpResponseRedirect('/home/')
            response = set_auth_cookies(response, user)
            return response

        except User.DoesNotExist:
            return render(request, 'auth/login.html', {'error': 'invalid email or password'})
    else:
        return Http404()


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
            response = HttpResponseRedirect('/home/')
            response = set_auth_cookies(response, user)
            return response

        except IntegrityError:
            return render(request, 'auth/register.html', {'error': 'username already taken'})

    else:
        return Http404()


def home(request: HttpRequest):
    if request.method == "GET":
        try:
            validate_user(request)
            return render(request, 'main/home.html')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')
    else:
        return Http404()


def rules(request: HttpRequest):
    if request.method == 'GET':
        try:
            validate_user(request)
            return render(request, 'main/rules.html')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')
    else:
        return Http404()


def about(request: HttpRequest):
    if request.method == 'GET':
        try:
            validate_user(request)
            return render(request, 'main/about.html')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')
    else:
        return Http404()
