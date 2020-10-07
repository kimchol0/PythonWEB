from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 渲染登录页面
from .models import *


def index_view(request):
    # 根据不同的请求方式处理不同的业务需求
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 接收请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        # 非空判断
        if uname and pwd:
            # 创建模型对象
            stu = Student(sname=uname, spwd=pwd)
            # 插入数据库
            stu.save()
            # 页面响应
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')


# 处理登录功能
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        # 查询数据库
        if uname and pwd:
            c = Student.objects.filter(sname=uname, spwd=pwd).count()
        # 判断是否登录成功
        if c == 1:
            return HttpResponse('登录成功！')
        return HttpResponse('登录失败！')


def show_view(request):
    # 查询stu_student表中所有数据
    stus = Student.objects.all()
    return render(request, 'show.html', {'students': stus})  # 注意,key:value中的key必须和前段对应，value必须和上面的变量名相同
