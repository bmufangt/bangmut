#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect


def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('uid'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_fun
"""
127.0.0.1:8000/200/?q=草莓＆page=2
.get_path    /200
.get_full_path: /200/?p=草莓&page=2
"""