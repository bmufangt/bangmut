#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from django.db import models
from models import *
from ttsx_goods.models import *
from ttsx_user.user_decorator import *
# Create your views here.

@login
def car(request):
    userid = request.session.get('uid')
    print ('userid%s'%userid)
    ucar_goods = UserCar.objects.filter(cuser_id=userid)
    count = len(ucar_goods)
    ucar_goods_list =[]
    for g in ucar_goods:
        goodsinfo = GoodsInfo.objects.filter(pk=g.cgoods_id).values()
        # print("="*50)
        dict = goodsinfo[0]
        try:
            dict['gcount'] = g.cgoodsnum
            # print(dict['gcount'])
            # print(dict)
        except Exception as e:
            print(e)
        # print(goodsinfo[0]['count'])
        ucar_goods_list.append(dict)


    # print(goodsinfo[0]['count'])
    # print('222222')
    context = {'title':'购物车', 'has_car':1,'ucar_goods_list':ucar_goods_list,'car_count':count}
    return render(request, 'ttsx_car/cart.html',context)

def modifycar_handle(request):
    goodsid = request.POST.get('goodsid')
    goodsnum = request.POST.get('goodsnum')

    print(goodsid,goodsnum)
    userid = request.session.get('uid')
    ucar = UserCar.objects.filter(cgoods_id=goodsid,cuser_id=userid)
    # print(ucar)
    # print(ucar)
    if len(ucar)==1:
        ucar[0].cgoodsnum = int(goodsnum)
        ucar[0].save()
    else:
        ucar = UserCar()
        ucar.cgoodsnum = int(goodsnum)
        ucar.cuser_id = int(userid)
        ucar.cgoods_id = int(goodsid)
        ucar.save()
    count = len(UserCar.objects.filter(cuser_id=userid))
    return JsonResponse({'count':count})

def delcar_handle(request):
    goodsnum = request.POST.get('goodsnum',1)
    goodsid =request.POST.get('goodsid')
    userid = request.session.get('uid')
    print(goodsid)
    print(goodsnum)
    usercar = UserCar.objects.filter(cgoods_id=goodsid,cuser_id=userid)
    if len(usercar) ==1:
        print('delete')
        usercar[0].delete()
        return render(request, 'ttsx_car/cart.html')
    print('end')
