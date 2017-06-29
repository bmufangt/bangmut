from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('ttsx_user.UserInfo')
    odate = models.DateField(auto_now=True)
    oispay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=6,decimal_places=2)
    oaddr = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('ttsx_goods.GoodsInfo')
    order = models.ForeignKey('OrderInfo')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.IntegerField()