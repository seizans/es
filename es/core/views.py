# coding=utf8

from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'from_hello_view': 'hoge'})
