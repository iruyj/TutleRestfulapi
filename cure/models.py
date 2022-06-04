import datetime

from django.db import models

# Create your models here.
class Cure(models.Model):
    created = models.DateField(verbose_name='해당날짜',auto_now_add=True)
    start = models.TimeField(verbose_name='시작시간',default=datetime.time)   # 처음 생성시간
    end = models.TimeField(verbose_name='완료시간',null=True)
    stretch = models.IntegerField(verbose_name='해당스트레칭번호')     # 몇번째 스트레칭인지
    status = models.IntegerField(verbose_name='현재상태')      # 완료인지 현재 개수
    user_email = models.EmailField(default=False,null=False)

    class Meta:
        db_table = 'cure'
        ordering = ['created','start']
        verbose_name = '스트레칭 테이블'

