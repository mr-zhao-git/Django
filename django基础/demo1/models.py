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
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)  # auto_now=True：当数据添加/更新是，设置当前时间为默认值

    class Meta:
        db_table = 't_emp'
        verbose_name = '员工表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        #   get_ +属性名 +_display
        return f'当前的员工是：{self.name},职位：{self.get_job_display()}'


# 部门的模型类，之间存在有层级关系（一对多）
# 一个类，内部之间的一对多关系，也称为树形结构模型类
class DeptModel(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='部门名称')
    address = models.CharField(max_length=100, unique=True, verbose_name='部门地址')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)  # auto_now=True：当数据添加/更新是，设置当前时间为默认值

    class Meta:
        db_table = 't_demp'
        verbose_name = '部门表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        #   get_ +属性名 +_display
        return f'当前的部门是：{self.name}'
