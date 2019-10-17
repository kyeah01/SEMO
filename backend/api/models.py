from django.db import models

# Create your models here.
class ApiList(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField()