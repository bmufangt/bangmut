from django.db import models

# Create your models here.
class UserCar(models.Model):
    cgoodsnum = models.IntegerField()
    cuser = models.ForeignKey('ttsx_user.UserInfo')
    cgoods = models.ForeignKey('ttsx_goods.GoodsInfo')
