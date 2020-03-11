import os
import django
from timeit import Timer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_dj.settings")
django.setup()

from django.conf import settings
from django.test import TestCase
import yaml, random
from django.conf import settings
from django.db.models import Value
from django.db.models.functions import Concat
from juheapp.models import User, App


# # 读取yaml配置文件
# filepath = r'D:\study\project__\django_333\first_dj\first_dj\myappconfig.yaml'
# with open(filepath, 'r', encoding='utf8') as f:
#     res = yaml.load(f, Loader=yaml.FullLoader)
#     print(res)
#     print(type(res))

# # static_file_path = os.path.join(settings.BASE_DIR,'static')
# #
# # print('static_file_path:', static_file_path)
# # filename = r'/abc.png'
# # filepath = os.path.join(static_file_path, filename)
# # print(filepath)
# print('basedir:', settings.BASE_DIR)
#
# static_filedir = settings.STATIC_URL
# # print('static_filedir',static_filedir)
# print('static_filedir', os.path.join(settings.BASE_DIR, 'static'))
# print(settings.STATIC_ROOT)
#

# 随机字符串
def ranstr(length):
    CHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(length):
        salt += random.choice(CHS)
    return salt


# 添加一个用户
def add_one():
    # 1
    user = User(openid='test_openid', nickname='new_user1')
    user.save()
    # 2
    User.objects.create(openid='test_openid2', nickname='new_user2')


# add_one()


# 批量增加
def add_batch():
    new_user_list = []
    for i in range(10):
        open_id = ranstr(32)
        nickname = ranstr(10)
        user = User(open_id=open_id, nickname=nickname)
        new_user_list.append(user)
    User.objects.bulk_create(new_user_list)


# 改一个
def modify_one():
    user = User.objects.get(openid='test_openid11')
    user.nickname = 'test_openid1111'
    user.save()


# modify_one()
# python manage.py sglmigrate 0006_auto_20200309_2044

def lazy_load():
    for user in User.objects.all():
        print(123, user.menu.all())


# 查询一条数据时,懒加载

# 预加载
def pre_load():
    for user in User.objects.prefetch_related('menu'):
        print(234, user.menu.all())


if __name__ == '__main__':
    t1 = Timer('lazy_load()', 'from __main__ import lazy_load')
    t2 = Timer('pre_load()', 'from __main__ import pre_load')
    print('懒加载:', t1.timeit(1000), '预加载加载:', t2.timeit(1000))
