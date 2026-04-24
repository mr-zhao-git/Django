from django.shortcuts import render

from demo1.models import Employee


# Create your views here.

def test1(request):
    emp = Employee.objects.get(pk=1)

    # 传入一个列表和字典的嵌套
    date1 = Employee.objects.filter(sal__gt=5000).values('id', 'name', 'sal')
    return render(request, 'html/test1.html', locals())


def test2(request):
    emp = Employee.objects.get(pk=1)

    # 传入一个列表和字典的嵌套
    date1 = Employee.objects.filter(sal__gt=5000).values('id', 'name', 'sal')
    return render(request, 'html/test2.html', locals())
