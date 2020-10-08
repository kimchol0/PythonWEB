from django.shortcuts import render
from .models import *
import math


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
