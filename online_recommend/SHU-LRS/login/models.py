from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.
class User(models.Model):
    '''用户表'''
    real_id = models.CharField(max_length=128,unique=True)
    student_id = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    gpa = models.CharField(max_length=256)
    score = models.CharField(max_length=256)
    gpa_lessons = models.CharField(max_length=256)
    gpa_reasons = models.CharField(max_length=256)
    score_lessons = models.CharField(max_length=256)
    score_reasons = models.CharField(max_length=256)
 
    def __str__(self):
        return self.student_id