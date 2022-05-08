from django.db import models

# Create your models here.
class Cure(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    completed = models.IntegerField()   # 완료 시 걸린 총 시간
    stretch1 = models.IntegerField()    # 첫번째 스트레칭 개수
    stretch2 = models.IntegerField()    # 두번째 스트레칭 개수
    stretch3 = models.IntegerField()    # 세번째 스트레칭 개수

    class Meta:
        ordering = ['created']