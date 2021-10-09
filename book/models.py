from django import forms
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    publish_date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0)

