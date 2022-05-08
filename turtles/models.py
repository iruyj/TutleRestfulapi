from django.db import models

# Create your models here.


class Turtle(models.Model):
    name = models.CharField(max_length=20)
    num = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'turtle'
        verbose_name = '유저 거북이 테이블'