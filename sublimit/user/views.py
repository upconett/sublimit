from django.http import *
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from .models import *
from forum.models import Article


@validate_user
def redirector(request: HttpRequest):
    if request.method == "GET":
        user = get_user(request)
        return redirect(f'/user/{user.username}/')
    else:
        raise Http404()


@validate_user
def show_user(request: HttpRequest, username: str):
    if request.method == "GET":
        me = get_user(request)
        user = User.objects.get(username=username)
        articles = [x for x in Article.objects.filter(author=user)]
        try: Follow.objects.get(follower=me, followed=user); followed = 'True'
        except Follow.DoesNotExist: followed = 'False'
        context = {
            'user': user,
            'contacts': ['github'],
            'articles': articles,
            'followed': followed,
        }
        if me == user:
            return render(request, 'user/my_profile.html', context)
        else:
            return render(request, 'user/profile.html', context)

    else:
        raise Http404()


@validate_user
def follow_user(request: HttpRequest, username: str):
    if request.method == "POST":
        me = get_user(request)
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
    else:
        raise Http404()


@validate_user
def settings(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'user/settings.html')
    elif request.method == "POST":
        # try:
        #     validate_user(request)
        # except InvalidCookie: return redirect('/login/')
        # except User.DoesNotExist: return redirect('/login/')
        pass
    else:
        raise Http404()
