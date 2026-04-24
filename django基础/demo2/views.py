from django.shortcuts import render


# Create your views here.

# 定义一个视图函数
def test_dtl1(request):
    return render(request, 'demo/dtl1.html')


def test_dtl2(request):
    pass