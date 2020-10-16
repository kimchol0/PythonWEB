from django.db import models


# python manage.py makemigrations stu
# python manage.py migrate

# 班级主表（一）
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)


# 学生表（从表）（多）
class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cno = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def __str__(self):
        return u'Student:%s' % self.sname


class Course(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return u'Course:%s' % self.course_name


class Teacher(models.Model):
    tno = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=30)
    cour = models.ManyToManyField(Course)

    def __str__(self):
        return u'Teacher:%s' % self.tname


# insertData('B203HTML5班','zhangjie','xiena')
# 以下内容在Python Console中输入，不要忘记from stu.models import *
def insertData(clsname, *snames):
    try:
        cls = Clazz.objects.get(cname=clsname)
    except Clazz.DoesNotExist:
        cls = Clazz.objects.create(cname=clsname)
        for sn in snames:
            try:
                stu = Student.objects.get(sname=sn)
            except Student.DoesNotExist:
                Student.objects.create(snamme=sn, cno=cls)


# insertData2('wangwu','Oracle','MySql')
# 以下内容在Python Console中输入，不要忘记from stu.models import *
def insertData2(tname, *coursenames):
    try:
        t = Teacher.objects.get(tname=tname)
    except Teacher.DoesNotExist:
        t = Teacher.objects.create(tname=tname)
        courseList = []
    for cn in coursenames:
        try:
            cou = Course.objects.get(course_name=cn)
        except Course.DoesNotExist:
            cou = Course.objects.create(course_name=cn)
            courseList.append(cou)
        t.cour.add(*courseList)
