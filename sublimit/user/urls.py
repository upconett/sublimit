from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.redirector),
    re_path('(?P<username>[-\w]+)/follow/', views.follow_user),
    re_path('(?P<username>[-\w]+)/', views.show_user),
    path('settings/', views.settings),
]