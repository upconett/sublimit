from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirector),
    path('home/', views.home),
    path('login/', views.login),
    path('register/', views.register)
]