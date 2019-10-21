from django.db import models

# nosql설정을 위해서
from djangotoolbox.fields import *


# Create your models here.
# 2019.10.21 PM 6:00
# embeddedModelField setting을 위한 작업 필요.
# dictField를 embeddedModelField로 교체하고 해당 Field에 들어갈
# 추상클래스를 정의해야함.
class VersionData(models.Model):
    content = models.TextField()

class APIList(models.Model):
    title = DictField()
    url = DictField()
    category = DictField()
    description = DictField()
    maxRequestCount = DictField()
    expiredDate = DictField()
    
    class Meta:
        abstract = True

class DataList(APIList):
    ratings = DictField()
    contributors = DictField()

class EditedList(APIList):
    requestUser = DictField()