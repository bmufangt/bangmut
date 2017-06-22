from django.contrib import admin
import models


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['ttitle','isDelete']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle','gprice','gtype_id']
    list_per_page = 8
# Register your models here.
admin.site.register(models.TypeInfo, TypeInfoAdmin)
admin.site.register(models.GoodsInfo,GoodsInfoAdmin)