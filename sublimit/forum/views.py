from django.http import *
from django.shortcuts import render, redirect

from utility.functions import *
from utility.exceptions import *

from .models import *
from user.models import *


@validate_user
def redirector(request: HttpRequest):
    if request.method == "GET":
        articles = []
        for a in Article.objects.all()[:10]:
            articles.append(a)
        context = {
            'articles': articles
        }
        return render(request, 'forum/main.html', context)

    else:
        raise Http404()


@validate_user
def new_article(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'forum/edit.html')
    elif request.method == "POST":
        pass
    else:
        raise Http404()


@validate_user
def show_article(request: HttpRequest, article_id: int):
    if request.method == "GET":
        article = Article.objects.get(id=article_id)
        return render(request, 'forum/article.html', {'article': article})
    else:
        raise Http404()


@validate_user
def edit_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def delete_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def comment_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def like_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def dislike_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def star_article(request: HttpRequest, article_id: int):
    pass
