from django.db import models


# Create your models here.
class UserScore(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    id_card = models.CharField(max_length=18, verbose_name='身份证号')
    exam_id = models.CharField(max_length=20, verbose_name='准考证号码')
    score_theory = models.CharField(max_length=20, verbose_name='理论成绩')
    score_major = models.CharField(max_length=20, verbose_name='专业成绩')
    score_case = models.CharField(max_length=20, verbose_name='案例成绩')
    score_major_total = models.CharField(max_length=20, verbose_name='专业总成绩')

    def __str__(self):
        return f'{self.name}  ({self.id_card})'
