# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(unique=True, max_length=100)
    mdesc = models.TextField(blank=True, null=True)
    ming = models.CharField(max_length=120)
    mlink = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'movie'

'''
生成逆向模型类的CMD命令
python manage.py inspectdb>movie/models.py
会将数据库中所有表都映射到模型类中
此时需要删除不需要的内容
比如本应用只需要movie表中的内容
故删除了其它的映射代码
'''