from django.shortcuts import render
from .models import *
import math
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.

def page(num, size=18):
    # 接收当前页码数
    num = int(num)  # 前台接收的参数num是字符串类型，必须转换为int类型

    # 总记录数
    totalRecords = Movie.objects.count()
    # 总页数
    totalPages = int(math.ceil(totalRecords * 1.0 / size))

    # 判断是否越界
    if num < 1:
        num = 1
    if num > totalPages:
        num = totalPages

    # 计算出每页显示的记录
    movies = Movie.objects.all()[((num - 1) * size):(num * size)]

    return movies, num


# 原生分页
def index_view(request):
    # 接收请求参数num
    num = request.GET.get('num', 1)

    # 处理分页请求
    movies, n = page(num)

    # 上一页的页码
    pre_page_num = n - 1
    # 下一页的页码
    next_page_num = n + 1

    return render(request, 'index01.html', {'movies': movies,
                                            'pre_page_num': pre_page_num,
                                            'next_page_num': next_page_num})


# Django分页
def index2_view(request):
    # 获取当前页码数
    num = request.GET.get('num', 1)
    n = int(num)
    # 查询所有数据
    movies = Movie.objects.all()
    # 创建分页器对象
    pager = Paginator(movies, 18)
    # 获取当前页的数据
    try:
        perpage_data = pager.page(n)
    except PageNotAnInteger:
        # 返回第一页的数据
        perpage_data = pager.page(1)
    except EmptyPage:
        # 返回最后一页的数据
        perpage_data = pager.page(pager.num_pages)
    return render(request,'index01.html',{'pager':pager,
                                          'perpage_data':perpage_data})
