from django.db import models


# Create your models here.

class Student(models.Model):  # 必须继承模型类，否则就是一个普通的类。否则无法对数据库进行操作
    sname = models.CharField(max_length=30, unique=True)  # sname相当于数据库中的字段
    spwd = models.CharField(max_length=30)

    def __str__(self):
        return u'Student:%s' % self.sname  # admin管理页面显示Student:对应的姓名，而非显示Student Object
