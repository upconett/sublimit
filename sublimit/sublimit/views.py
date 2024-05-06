from django.http import *
from django.shortcuts import render

def show_test(request: HttpRequest):
    return render(request, 'test/test.html')
