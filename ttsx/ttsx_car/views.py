#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.


def car(request):
    context = {'title':'购物车', 'has_car':1}
    return render(request, 'ttsx_car/cart.html',context)
