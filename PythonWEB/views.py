from django.http import HttpResponse


# 显示Hello World
def index_view(request):
    return HttpResponse('Hello World')
