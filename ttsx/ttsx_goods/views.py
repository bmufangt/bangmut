#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    types = TypeInfo.objects.all()
    type0 = types[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = types[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = types[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = types[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = types[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = types[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = types[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = types[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = types[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = types[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = types[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = types[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {'title':'首页','has_car':1,
               'type0':type0,'type01':type01,
               'type1':type1,'type11':type11,
               'type2':type2,'type21':type21,
               'type3':type3,'type31':type31,
               'type4':type4,'type41':type41,
               'type5':type5,'type51':type51,
               }
    return render(request, 'ttsx_goods/index.html',context)

def list(request,tid,pindex,sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))

    #默认排序，最新　sort=1
    if sort == '1':
        type_list = typeinfo.goodsinfo_set.order_by('-id')
    #　价格
    if sort == '2':
        type_list = typeinfo.goodsinfo_set.order_by('-gprice')
    #　人气
    if sort == '3':
        type_list = typeinfo.goodsinfo_set.order_by('-gclick')

    p = Paginator(type_list,8)
    goods = p.page(int(pindex))
    context = {'title': '首页',
               'has_car': 1,
                'type': goods,
                'sort': sort,
                'pindex': int(pindex),
                'typeinfo':typeinfo,
               }
    return render(request,'ttsx_goods/list.html',context)


def detail(request,id):
    goods = GoodsInfo.objects.get(pk=id)
    goods.gclick = goods.gclick + 1
    goods.save()
    type = TypeInfo.objects.get(id=goods.gtype_id)
    type0 = type.goodsinfo_set.order_by('-id')[0:2]
    # type1 = types[1].goodsinfo_set.order_by('-id')
    # type2 = types[2].goodsinfo_set.order_by('-id')
    # type3 = types[3].goodsinfo_set.order_by('-id')
    # type4 = types[4].goodsinfo_set.order_by('-id')
    # type5 = types[5].goodsinfo_set.order_by('-id')
    context = {'title': '首页', 'has_car': 1,
               'goods': goods,
               'type': type0,
               # 'type1': type1,
               # 'type2': type2,
               # 'type3': type3,
               # 'type4': type4,
               # 'type5': type5,
               }
    return render(request,'ttsx_goods/detail.html',context)