from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 渲染登录页面
def index_view(request):
    return render(request, 'login.html')  # 渲染页面


# 处理登录功能
def login_view(request):
    # 接收表单的请求参数
    uname = request.GET.get('uname', '')  # 这里的uname表示网页表单中name为uname的input，逗号后面的表示为空
    pwd = request.GET.get('pwd', '') # 这里的pwd表示网页表单中name为pwd的input，逗号后面的表示为空
    # 判断
    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('登陆成功！')
    return HttpResponse('登陆失败！')
