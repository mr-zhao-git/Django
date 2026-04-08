import datetime

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_http_methods


# Create your views here.


# 写视图函数的地方
def hello(request):
    print('hello')
    # return HttpResponse('hello')
    return JsonResponse({'hello': 'world'})


def test1(request):
    print('test1')
    return HttpResponse('test1')


def test2(request, arg1, arg2):
    print(arg1)
    print(arg2)
    return HttpResponse('test2')


def test3(request, month, year):
    print(month)
    print(year)
    return HttpResponse(test3)


def test4(request):
    request_path = reverse('zhao-test3', kwargs={'year': 2020, 'month': 12})
    print(request_path)
    # return HttpResponse('test4')
    return redirect(request_path)


# 定义视图类
class MyView(View):
    def get(self, request):
        print(request.GET)  # 打印get请求的所有传参
        print(request.POST)  # 打印表单请求的所有传参
        print(request.body)  # 打印post的json请求的所有传参
        return HttpResponse('MyView-get')

    def post(self, request):
        print(request.GET)  # 打印get请求的所有传参
        print(request.POST)  # 打印表单请求的所有传参
        print(request.body)  # 打印post的json请求的所有传参
        return HttpResponse('MyView-post')

    def put(self, request):
        pass

    def delete(self, request):
        pass


@require_http_methods({'GET', 'POST'})  # 通过装饰器来进行限制请求方式
def test6(request):
    """可以接收GET、POST两种方式"""
    print(request.GET)
    print(request.POST)
    return HttpResponse('test6')


@require_http_methods({'GET', 'POST', 'PUT', 'DELETE'})
def test7(request):
    """可以接收GET、POST两种方式"""
    print(request.GET)
    print(request.POST)
    return HttpResponse('test6')


@require_http_methods({'GET'})
def test8(request):
    """重定向"""
    print('test8')
    username = request.GET.get('username')
    print(username)
    return HttpResponse('test1')


@require_http_methods({'GET'})
def test9(request):
    """渲染模板"""
    print('test9')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # return render(request, 'test9.html', {'now_time': now_time})  # 第一个参数必须是request，第二个参数是模板
    return render(request, 'test9.html', locals())  # 表示将函数中所有的临时变量都传入到模板中


@require_http_methods({'POST'})
def test10(request):
    """请求头"""
    print('test10')
    return HttpRequest.META.get('HTTP_HOST')


def login(request):
    return render(request, "login.html")


def auth(request):
    #  获取数据
    print("request.POST:", request.POST)

    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    # 模拟数据校验
    if user == "laomao" and pwd == "123456":
        # return HttpResponse("验证通过")
        return redirect("/users/")
    else:
        # return HttpResponse("用户名或者密码错误")
        # return redirect("/users/login")
        # 重定向适合动态页面 静态页面可以用render
        # 静态页面渲染一些信息一般用render
        msg = "用户名或者密码错误"
        return render(request, "login.html", {"msg": msg})
