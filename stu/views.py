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
    # 接收表单的请求参数
    uname = request.GET.get('uname', '')  # 这里的uname表示网页表单中name为uname的input，逗号后面的表示为空
    pwd = request.GET.get('pwd', '')  # 这里的pwd表示网页表单中name为pwd的input，逗号后面的表示为空
    # 判断
    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('登陆成功！')
    return HttpResponse('登陆失败！')


def show_view(request):
    # 查询stu_student表中所有数据
    stus = Student.objects.all()
    return render(request, 'show.html', {'students': stus})  # 注意,key:value中的key必须和前段对应，value必须和上面的变量名相同
