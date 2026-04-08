from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django_orm.models import PersonModel


def test_db(request):
    # test_new()  # 测试新增
    # test_all()
    # test_get()
    # test_filter()
    # test_exclude()
    # test_order_by()
    # test_exists()
    # test_values()
    test_values_list()
    return HttpResponse('测试数据库操作')


def test_new():
    """新增操作"""
    # 1、方法一
    p = PersonModel(name='张三', age=18)
    p.save()

    # 2、方法二
    PersonModel.objects.create(name='李四', age='18')


def test_all():
    """查询所有"""
    result = PersonModel.objects.all()
    for item in result:
        print(item)


def test_get():
    """查询指定主键的数据"""
    # result = PersonModel.objects.get(id=1)
    result = PersonModel.objects.get(pk=1)  # django框架中主键默认都有一个别名：pk
    print(result)

def test_filter():  #默认返回的数据是列表
    """过滤查询指定的数据"""
    result = PersonModel.objects.filter(age__gt=15)     #年龄大于15岁的人
    for item in result:
        print(item)

def test_exclude():
    """过滤查询指定以外的数据"""
    result = PersonModel.objects.exclude(name = '张三')    #查询名字不是张三的
    for item in result:
        print(item)

def test_order_by():
    """查询数据排序"""
    result = PersonModel.objects.all().order_by('age')    #升序
    result = PersonModel.objects.all().order_by('-age')    #降序
    for item in result:
        print(item)

def test_exists():
    """判断查询集中是否有数据"""
    print( PersonModel.objects.filter(name='张三').exists())


def test_values():
    """值返回所有人员的名字"""
    result = PersonModel.objects.values('id','name')    #只返回两个
    #result是列表和字典的嵌套
    for dct in result:
        print(dct['id'],dct['name'])

def test_values_list():
    """值返回所有人员的名字"""
    result = PersonModel.objects.values_list('id','name')    #只返回两个
    #result是列表和元组的嵌套,字段的名字不在结果中
    for lst in result:
        print(lst[0],lst[1])