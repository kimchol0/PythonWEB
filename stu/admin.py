from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
# 然后在CMD中创建超级用户 python manage.py createsuperuser输入用户名邮箱密码 admin 1@1.com 123
admin.site.register(Post)
