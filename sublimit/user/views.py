from django.http import *
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from .models import *


def redirector(request: HttpRequest):
    if request.method == "GET":
        try:
            user = validate_user(request)
            return redirect(f'/user/{user.username}/')

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')

    else:
        raise Http404()


def show_user(request: HttpRequest, username: str):
    if request.method == "GET":
            try:
                me = validate_user(request)
                user = User.objects.get(username=username)
                context = {
                    'user': user,
                    'contacts': ['github'],
                    'followed': False,
                }
                if me == user:
                    return render(request, 'user/my_profile.html', context)
                else:
                    return render(request, 'user/profile.html', context)
                
            except InvalidCookie: return redirect('/login/')
            except User.DoesNotExist: return redirect('/login/')

    else:
        raise Http404()


def follow_user(request: HttpRequest, username: str):
    if request.method == "POST":
        try:
            me = validate_user(request)
            user = User.objects.get(username=username)

            try:
                follow = Follow.objects.get(
                    follower = me,
                    followed = user
                )
                follow.delete()
                context = '{ "followed": "False" }'
                print('deleted', follow)
            except Follow.DoesNotExist:
                follow = Follow.objects.create(
                    follower = me,
                    followed = user
                )
                context = '{ "followed": "True" }'
                print('created', follow)
            return HttpResponse(context)

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')
    else:
        raise Http404()


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
        raise Http404()
