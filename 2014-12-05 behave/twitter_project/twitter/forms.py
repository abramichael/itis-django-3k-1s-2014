from django import forms
from django.contrib.auth.models import User
class TweetForm(forms.Form):
	text = forms.CharField(max_length=140, widget=forms.Textarea)

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserSettingsForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name", "last_name", "email"]