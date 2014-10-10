from django.db import models

class RawTweet(models.Model):
    text = models.CharField(max_length=140)
    p_date = models.DateTimeField()
