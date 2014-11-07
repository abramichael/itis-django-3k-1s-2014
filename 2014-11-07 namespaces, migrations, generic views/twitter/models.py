from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=140)
    p_date = models.DateTimeField()
