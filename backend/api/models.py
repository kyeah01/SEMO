from django.db import models
from django.contrib.auth import get_user_model

from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()

# 2019.10.22 PM 2:23
# 보여줄 확정 정보 / request를 받을 정보를 담을 model의 구조가 비슷하므로
# 이를 상속시켜줄 model APIList 구현.
class Category(models.Model):
    name = models.CharField(max_length=140)

class APIList(models.Model):
    title = models.TextField()
    url = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    howToUse = models.TextField() 
    maxRequestCount = models.TextField()
    expiredDate = models.TextField()
    
    class Meta:
        abstract = True

class APISite(APIList):
    contributors = models.ManyToManyField(User)

class EditedList(APIList):
    target = models.ForeignKey(APISite, on_delete=models.CASCADE)
    requestUser = models.ManyToManyField(User)
    check = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)

class EndPoints(models.Model):
    apisite = models.ForeignKey(APISite, on_delete=models.CASCADE)
    isAuthentication = models.BooleanField()
    method = models.CharField(max_length=30)
    name = models.TextField()
    pathParams = models.TextField()
    queryString = models.TextField()
    response = models.TextField()

class RegisterList(APIList):
    requestUser = models.ManyToManyField(User)

class Ratings(models.Model):
    apiSite = models.ForeignKey(APISite, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    rating_date = models.CharField(max_length=200)

class GuideCode(models.Model):
    lang = models.CharField(max_length=10)
    code = models.TextField()