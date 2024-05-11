from django.urls import path, re_path

from . import views

regex = "(?P<article_id>\d+)"

urlpatterns = [
    path('', views.redirector),
    path('article/new/', views.new_article),
    re_path(f'article/{regex}/edit', views.edit_article),
    re_path(f'article/{regex}/delete', views.delete_article),
    re_path(f'article/{regex}/comment', views.comment_add),
    re_path(f'article/{regex}/like', views.like_article),
    re_path(f'article/{regex}/dislike', views.dislike_article),
    re_path(f'article/{regex}/star', views.star_article),
    re_path(f'article/{regex}', views.show_article)
]