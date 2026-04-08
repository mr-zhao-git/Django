from datetime import date

from django.db import models


# Create your models here.

class JobChoices(models.TextChoices):
    """枚举类"""
    MR = 'MR', '部门经理'
    CE = 'CE', '普通职员'
    PR = 'PR', '总裁'


# 员工的模型类
class Employee(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='员工姓名')
    job = models.CharField(choices=JobChoices.choices, max_length=2, default=JobChoices.CE, verbose_name='员工姓名')
    entry_date = models.DateField(default=date.today(), verbose_name='入职时间')
    sal = models.IntegerField(verbose_name='级别薪资')
    bonus = models.SmallIntegerField(default=0, verbose_name='津贴')
    is_leave = models.BooleanField(default=False, verbose_name='是否离职')

    class Meta:
        db_table = 't_emp'
        verbose_name = '员工表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        #   get_ +属性名 +_display
        return f'当前的员工是：{self.name},职位：{self.get_job_display()}'