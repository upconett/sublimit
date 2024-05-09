from django.http import *
from django.shortcuts import redirect

from .exceptions import InvalidCookie

from user.models import User


def get_auth_cookies(request: HttpRequest) -> tuple[str, str, str]:
    username = request.get_signed_cookie('username', None)
    email = request.get_signed_cookie('email', None)
    password = request.get_signed_cookie('password', None)
    if any( cooke is None 
            for cooke in [username, email, password]):
        raise InvalidCookie
    return (username, email, password)


def get_auth_login(request: HttpRequest) -> tuple[str, str]:
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    if any( element is None 
            for element in [email, password]):
        raise KeyError
    return (email, password)


def get_auth_register(request: HttpRequest) -> tuple[str, str, str]:
    username = request.POST.get('username', None)
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    if any( element is None 
            for element in [username, email, password]):
        raise KeyError
    return (username, email, password)


def set_auth_cookies(response: HttpResponseRedirect, user: User) -> HttpResponseRedirect:
    response.set_signed_cookie('username', user.username)
    response.set_signed_cookie('email', user.email)
    response.set_signed_cookie('password', user.password)
    return response


def validate_user(view_function):
    '''Decorator that redirects to `/login/` if user is invalid'''
    def wrapper(request: HttpRequest, *args, **kwargs):
        try:
            username, email, password = get_auth_cookies(request)
            User.objects.get(
                username=username,
                email=email,
                password=password
            )
            return view_function(request, *args, **kwargs)
        except InvalidCookie: return redirect('/login/')
        except User.DoesNotExist: return redirect('/login/')
    return wrapper


def get_user(request: HttpRequest) -> User:
    '''Return User object found by cookies'''
    username, email, password = get_auth_cookies(request)
    return User.objects.get(
        username=username,
        email=email,
        password=password
    )