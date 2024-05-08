from django.http import *
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *


def redirector(request: HttpRequest):
    if request.method == "GET":
        try:
            user = validate_user(request)
            return redirect(f'/user/{user.username}/')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')

    else:
        return Http404()


def show_user(request: HttpRequest, username: str):
    if request.method == "GET":
        if username:
            try:
                user = User.objects.get(username=username)
                return render(request, 'user/profile.html', {'user': user})
            except User.DoesNotExist: return Http404()

        else:
            try:
                user = validate_user(request)
                return render(request, 'user/my_profile.html', {'user': user})

            except InvalidCookie: return Http404()
            except User.DoesNotExist: return Http404()

    else:
        return Http404()


def follow_user(request: HttpRequest, username: str):
    if request.method == "POST":
        # try: me = validate_user(request)
        # except InvalidCookie: return redirect('/login/')
        # except User.DoesNotExist: return redirect('/login/')

        # try: user = User.objects.get(username=username)
        # except User.DoesNotExist: return redirect('')
        pass
    else:
        return Http404()


def settings(request: HttpRequest):
    if request.method == "GET":
        try:
            validate_user(request)
            return render(request, 'user/settings.html')
        
        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')
    elif request.method == "POST":
        # try:
        #     validate_user(request)
        # except InvalidCookie: return redirect('/login/')
        # except User.DoesNotExist: return redirect('/login/')
        pass
    else:
        return Http404()
