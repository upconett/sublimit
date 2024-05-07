from django.http import *

from utility.exceptions import InvalidCookie


def get_auth_cookies(request: HttpRequest) -> tuple[str, str, str]:
    email = request.get_signed_cookie('email', None)
    username = request.get_signed_cookie('username', None)
    password = request.get_signed_cookie('password', None)
    if any( cooke is None 
            for cooke in [email, username, password]):
        raise InvalidCookie
    return (email, username, password)