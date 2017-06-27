# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_goods', '0001_initial'),
        ('ttsx_user', '0002_auto_20170621_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cgoodsnum', models.IntegerField()),
                ('cgoods', models.ForeignKey(to='ttsx_goods.GoodsInfo')),
                ('cuser', models.ForeignKey(to='ttsx_user.UserInfo')),
            ],
        ),
    ]
