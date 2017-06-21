#coding=utf-8

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40) #加密后长度
    uemail = models.CharField(max_length=30)
    urecvname = models.CharField(max_length=20,default='')
    urecvaddr = models.CharField(max_length=100,default='')
    uphone = models.CharField(max_length=11,default='')
