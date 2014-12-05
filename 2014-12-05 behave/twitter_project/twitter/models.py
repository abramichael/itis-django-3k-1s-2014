from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    text = models.TextField(max_length=140)
    published_on = models.DateTimeField()
    user = models.ForeignKey(User)

class UserInfo(models.Model):
	user = models.OneToOneField(User)
	MALE = "M"
	FEMALE = "F"
	genders = ((MALE, "Male"),(FEMALE, "Female"))
	gender = models.CharField(max_length=1, choices=genders,
		blank=True, default=FEMALE)
	avatar = models.ImageField(blank=True, upload_to="imgs")
	def __unicode__(self):
		return self.user.username+ ": User info"