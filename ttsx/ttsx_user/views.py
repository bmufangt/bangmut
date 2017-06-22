#coding=utf-8


from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
from models import *

# Create your views here.
def register(request):
    return render(request, 'ttsx_user/register.html',{'title':'注册'})


def register_handle(request):
    uname = request.POST.get('user_name')
    upwd = request.POST['pwd']
    upwd2 = request.POST['cpwd']
    uemail = request.POST['email']
    if upwd != upwd2:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd)
    #upwd3 = s1.hexdigest()
    upwd3 = s1.hexdigest()
    userinfo = UserInfo()
    userinfo.uname = uname
    userinfo.upwd = upwd3
    userinfo.uemail = uemail
    userinfo.save()
    return redirect('/user/login/')

def register_exists(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    context = {'title':'登录','errorname': 0,'errorpwd': 0}
    return render(request, 'ttsx_user/login.html',context)



def login_handle(request):
    print('1111')
    uname = request.POST.get('uname')
    upwd = request.POST['upwd']
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    #try:
    #    if UserInfo.objects.get(uname=uname).count():
    #        return redirect('/user/user_center_info/')
    #except:
    #    return redirect('/user/login/')
    users = UserInfo.objects.filter(uname=uname)

    if len(users) == 1:
        if upwd3 == users[0].upwd:
            request.session['uname'] = users[0].uname
            request.session['uemail'] = users[0].uemail
            context = {'title':'登录','errorname': 0,'errorpwd': 0}
            return JsonResponse(context)
        else:
            context = {'title':'登录','errorname': 0,'errorpwd': 1}
            return JsonResponse(context)
    else:
        print('hah')
        context = {'title':'登录','errorname': 1,'errorpwd': 0}
        return JsonResponse(context)


def user_center_info(request):
    uname = request.session.get('uname')
    uemail = request.session.get('uemail')
    return render(request,'ttsx_user/user_center_info.html',{'title':'个人中心','uname':uname,'uemail':uemail,"has_car":0})


def user_center_order(request):
    return render(request,'ttsx_user/user_center_order.html',{'title':'全部订单',"has_car":0})


def user_center_site(request):
    return render(request,'ttsx_user/user_center_site.html',{'title':'收货地址',"has_car":0})

def user_center_site_handle(request):
    users = UserInfo.objects.get(uname=request.session.get('uname'))

    if request.method =='POST':
        users.urecvname = request.POST.get('recvname')
        users.urecvaddr = request.POST.get('recvaddr')
        users.uphone = request.POST.get('phone')
        users.save()
    context = {'title':'收货地址','users':users,"has_car":0}
    return render(request, 'ttsx_user/user_center_site.html',context)

