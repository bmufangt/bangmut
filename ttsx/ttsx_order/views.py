#coding=utf-8
from django.shortcuts import render,redirect,render_to_response
from django.http.response import JsonResponse
from django.core.urlresolvers import resolve,reverse
import json
from ttsx_goods.models import *
from ttsx_user.models import *
from ttsx_user.user_decorator import *

def place_order(request):

    str = request.POST.get('str')
    request.session['str'] = str
    # list = eval(str)
    # userid = request.session.get('uid')
    # # print(type (dict))
    # # print(type(dict[0]))
    # for l in list:
    #     goods = GoodsInfo.objects.filter(id=l['goodsid']).values()
    #     print(goods)
    #     # print(x)
    # userbuy_goods_list = []
    # for l in list:
    #     goodsinfo = GoodsInfo.objects.filter(pk=l['goodsid']).values()
    #     # print("="*50)
    #     dict = goodsinfo[0]
    #     try:
    #         dict['gcount'] = l['goodsnum']
    #         # print(dict['gcount'])
    #         # print(dict)
    #     except Exception as e:
    #         print(e)
    #     # print(goodsinfo[0]['count'])
    #     userbuy_goods_list.append(dict)
    #
    # user = UserInfo.objects.filter(pk=userid)
    # print(user)
    # global context
    # context = {'title': '用户订单', 'has_order': 1, 'userbuy_goods_list': userbuy_goods_list,'user':user[0]}
    return redirect('/place_order_handle')
    # return render(request, 'ttsx_order/place_order.html',context)


# text = context
@login
def place_order_handle(request):
    str = request.session['str']
    list = eval(str)
    userid = request.session.get('uid')
    # print(type (dict))
    # print(type(dict[0]))
    for l in list:
        goods = GoodsInfo.objects.filter(id=l['goodsid']).values()
        print(goods)
        # print(x)
    userbuy_goods_list = []
    for l in list:
        goodsinfo = GoodsInfo.objects.filter(pk=l['goodsid']).values()
        # print("="*50)
        dict = goodsinfo[0]
        try:
            dict['gcount'] = l['goodsnum']
            # print(dict['gcount'])
            # print(dict)
        except Exception as e:
            print(e)
        # print(goodsinfo[0]['count'])
        userbuy_goods_list.append(dict)

    user = UserInfo.objects.filter(pk=userid)
    # print(user)
    # global context
    context = {'title': '用户订单', 'has_order': 1, 'userbuy_goods_list': userbuy_goods_list, 'user': user[0]}

    return render(request, 'ttsx_order/place_order.html',context)
