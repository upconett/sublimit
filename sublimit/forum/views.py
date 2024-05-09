from django.http import *
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from .models import *
from user.models import *


def redirector(request: HttpRequest):
    if request.method == "GET":
        try:
            user = validate_user(request)
            articles = []
            for a in Article.objects.all()[:10]:
                articles.append(a)
            context = {
                'articles': articles
            }
            return render(request, 'forum/main.html', context)

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')

    else:
        raise Http404()



def new_article(request: HttpRequest):
    if request.method == "POST":
        try:
            user = validate_user(request)

        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')

    else:
        raise Http404()


def show_article(request: HttpRequest):
    pass


def edit_article(request: HttpRequest):
    pass


def delete_article(request: HttpRequest):
    pass


def comment_article(request: HttpRequest):
    pass


def like_article(request: HttpRequest):
    pass


def dislike_article(request: HttpRequest):
    pass


def star_article(request: HttpRequest):
    pass
