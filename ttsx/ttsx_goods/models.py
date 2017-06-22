#coding=utf-8
from django.db import models
from tinymce_4.fields import TinyMCEModelField
# Create your models here.


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    # 静态文件，上传到　MEDIA_ROOT.ttsx_goods
    gimage = models.ImageField(upload_to='ttsx_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20)
    gclick = models.IntegerField()
    gabstract = models.CharField(max_length=200)
    ginventory = models.IntegerField()
    gdetails = TinyMCEModelField()
    gtype = models.ForeignKey('TypeInfo')