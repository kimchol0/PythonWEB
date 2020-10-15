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


# insertData('B203HTML5班','zhangjie','xiena')
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
