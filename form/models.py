from djongo import models
# Create your models here.
#ユーザ情報のDB情報
class UserInfo(models.Model):
    userName = models.CharField(max_length=200)
    country = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

class Entry(models.Model):
    userID = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class battledata(models.Model):
    battleID = models.CharField(max_length=50)
    userID1 = models.CharField(max_length=50)
    userID2 = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)