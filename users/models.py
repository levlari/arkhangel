# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    answers = models.TextField (default='.')
    isComplit  = models.BooleanField (default=False)
    points = models.IntegerField (default=0)
    curent_question = models.IntegerField (default=1)
    curent_test = models.IntegerField(default=1)
    time_begin = models.TimeField (auto_now=False, auto_now_add=False, default='00:00:00')