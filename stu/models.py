from django.db import models


# Create your models here.

class Student(models.Model):  # 必须继承模型类，否则就是一个普通的类。否则无法对数据库进行操作
    sname = models.CharField(max_length=30, unique=True)  # sname相当于数据库中的字段
    spwd = models.CharField(max_length=30)

    def __str__(self):
        return u'Student:%s' % self.sname  # admin管理页面显示Student:对应的姓名，而非显示Student Object


# 帖子模型类
class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10, unique=True)
    context = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    isdelete = models.BooleanField(default=False)
    access_count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    file = models.ImageField(upload_to='upload/images/')  # 如果上传文件为非图片则改为FileField

    def __str__(self):
        return u'Post:%s,%s' % (self.title, self.access_count)

    class Meta:
        db_table = 't_post'


# python manage.py makemigrations stu
# python manage.py migrate

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)

    def __str__(self):
        return u'Student:%s' % self.sname


class SCard(models.Model):
    student = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    major = models.CharField(max_length=30)

    def __str__(self):
        return u'Scard:%s' % self.major
