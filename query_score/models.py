from django.db import models


# Create your models here.
class UserScore(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    id_card = models.CharField(max_length=18, verbose_name='身份证号')
    exam_id = models.CharField(max_length=20, verbose_name='准考证号码')
    score_theory = models.FloatField(verbose_name='理论成绩')
    score_major = models.FloatField(verbose_name='专业成绩')
