from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirector),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('rules/', views.rules),
    path('about/', views.about)
]