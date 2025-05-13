from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class User(AbstractBaseUser):
    username=models.CharField("사용자 계정", max_length=20, unique=True)
    password=models.CharField("비밀번호",max_length=256)
# Create your models here.
