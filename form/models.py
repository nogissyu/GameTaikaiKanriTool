from djongo import models
# Create your models here.
#ユーザ情報のDB情報
class UserInfo(models.Model):
    userName = models.CharField(max_length=200)
    country = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)