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
        tag = request.GET.get('tag', None)
        search = request.GET.get('search', None)
        if tag: 
            for a in Article.objects.filter(tag=tag): articles.append(a)
        elif search: 
            for a in Article.objects.all(): 
                if any(search in x for x in [a.title.lower(), a.text.lower(), a.author.username.lower()]): articles.append(a)
        else:
            for a in Article.objects.all(): articles.append(a)
        context = { 
            'articles': articles,
            'user': get_user(request),
            'tag': tag
            }
        return render(request, 'forum/main.html', context)

    else:
        raise Http404()


@validate_user
def new_article(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'forum/edit.html', {'action': '/forum/article/new/'})
    elif request.method == "POST":
        article = create_article(request)
        return redirect(f'/forum/article/{article.id}/')
    else:
        raise Http404()


@validate_user
def show_article(request: HttpRequest, article_id: int):
    if request.method == "GET":
        article = Article.objects.get(id=article_id)
        comments = [c for c in Comment.objects.filter(article=article)]
        return render(request, 'forum/article.html', {'article': article, 'comments': comments})
    else:
        raise Http404()


@validate_user
def edit_article(request: HttpRequest, article_id: int):
    if request.method == "GET":
        article = Article.objects.get(id=article_id)
        return render(request, 'forum/edit.html', {'article': article, 'action': f'/forum/article/{article.id}/edit/'})
    elif request.method == "POST":
        article = alter_article(request)
        return redirect(f'/forum/article/{article.id}/')
    else:
        raise Http404()


@validate_user
def delete_article(request: HttpRequest, article_id: int):
    if request.method == "GET":
        Article.objects.get(id=article_id).delete()
        return redirect(f'/forum/')
    else:
        raise Http404()


@validate_user
def comment_add(request: HttpRequest, article_id: int):
    if request.method == "POST":
        user = get_user(request)
        article = Article.objects.get(id = article_id)
        Comment.objects.create(
            author=user,
            article=article,
            text=request.POST.get('text')
        )
        return redirect(f"/forum/article/{article.id}")

    else:
        raise Http404()



@validate_user
def like_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def dislike_article(request: HttpRequest, article_id: int):
    pass


@validate_user
def star_article(request: HttpRequest, article_id: int):
    pass
