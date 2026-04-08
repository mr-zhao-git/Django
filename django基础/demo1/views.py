from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, JobChoices
from datetime import date

# Create your views here.

def test_db2(request):
    # Employee.objects.create(name='zs',job=JobChoices.CE,entry_date = date(2019,10,19),sal=4500,bonus=600)
    # Employee.objects.create(name='ls',job=JobChoices.CE,entry_date = date(2020,12,19),sal=5500,bonus=800)
    # Employee.objects.create(name='ww',job=JobChoices.CE,entry_date = date(2017,11,19),sal=8000,bonus=1200)
    # Employee.objects.create(name='sl',job=JobChoices.CE,entry_date = date(2025,6,19),sal=3500,bonus=400)

    # result = Employee.objects.filter(name__contains='w') #模糊查询
    # result = Employee.objects.filter(entry_date__year=2025) #查询在2025年入职的所有员工
    query = Employee.objects.filter(Q(Q(entry_date__year=2025) | Q(Q(sal__gt=5000) & Q(bonus__gt=5000))))

    for emp in query:
        print(emp)

    return HttpResponse('test__db2')