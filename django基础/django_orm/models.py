from django.db import models
from django.db.models import Model

from django_orm.base_model import BaseModel

# Create your models here.
'''定义模型类'''
'''
数据库迁移命令：
    python manage.py makemigrations     #生成迁移文件
    python manage.py migrate
'''


# 创建第一个模型类
class PersonModel(BaseModel):
    # 所有模型类，orm提供一个默认的主键：id  类型是:Interger,同时是自增的
    # my_id = models.IntegerField(primary_key=True)       #自己定义一个主键
    name = models.CharField(max_length=20, unique=True, verbose_name='姓名')  # unique=True：唯一索引
    last_name = models.CharField(max_length=10, null=True, blank=True, verbose_name='姓')
    age = models.IntegerField(default=18, verbose_name='年龄')
    address = models.CharField(max_length=200, null=True, blank=True)


    class Meta:
        db_table = 't_person'
        verbose_name = '人员表'
        verbose_name_plural = verbose_name
        ordering = ['id']  # 默认排序采用的字段

    def __str__(self):
        return f'当前人员是：{self.name},年龄是：{self.age}'