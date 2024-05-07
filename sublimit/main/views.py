from django.http import *
from django.shortcuts import render, redirect

from sublimit.utility.functions import *
from sublimit.utility.exceptions import *


def redirector(request: HttpRequest):
    if request.method == "GET":
        try:
            email, username, password = get_auth_cookies(request)
        except InvalidCookie:
            return redirect('/login/')
    else:
        return Http404()


def home(request: HttpRequest):
    if request.method == "GET":
        pass
    else:
        return Http404()


def login(request: HttpRequest):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    else:
        return Http404()


def register(request: HttpRequest):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    else:
        return Http404()