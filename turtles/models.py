import datetime

from django.db import models

# Create your models here.


class Turtle(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateField(verbose_name='해당날짜',auto_now_add=True)
    ease = models.IntegerField(verbose_name='거북목 완화도', default=0)
    best = models.CharField(verbose_name='완주날짜',null=True, default="0000-00-00", max_length=20)
    num = models.IntegerField(verbose_name='거북이 캐릭터 번호')
    email = models.EmailField(verbose_name='사용자 식별 이메일',primary_key=True)

    class Meta:
        db_table = 'turtle'
        ordering = ['created']
        verbose_name = '유저 거북이 테이블'