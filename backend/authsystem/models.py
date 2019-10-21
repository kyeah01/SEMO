from django.db import models

# nosql설정을 위해서
from djangotoolbox.fields import *

# Create your models here.
class Profile(models.Model):
    api_update = DictField()
    ratings = DictField()