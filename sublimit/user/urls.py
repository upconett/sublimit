from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.redirector),
    re_path('(?P<username>[-\w]+)', views.show_user)
]