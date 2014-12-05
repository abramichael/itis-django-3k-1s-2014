from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from twitter.decorators import no_login_please
from twitter.forms import TweetForm, LoginForm, UserSettingsForm
from twitter.models import Tweet

from time import gmtime, strftime, mktime, strptime
import datetime

@login_required
def home(request):
	if request.method == "POST":
		canTweet = True
		error_tweet_30 = ""
		if request.session.has_key("time_of_last_tweet"):
			old_time = datetime.datetime.strptime(request.session["time_of_last_tweet"], 
					"%d %m %Y %H:%M:%S")

			delta = datetime.datetime.today() - old_time
			print datetime.datetime.today()
			print old_time
			print delta
			print delta.total_seconds()
			print delta.seconds
			if delta.total_seconds() < 30:
				canTweet = False
				error_tweet_30 = "You have tweeted " + str(int(delta.total_seconds())) + \
						" seconds ago."
		if canTweet:
			f = TweetForm(request.POST)
			if f.is_valid():
				t = Tweet()
				t.user = request.user
				t.text = f.cleaned_data["text"]
				d = datetime.datetime.today()
				t.published_on = d
				t.save()
				request.session["time_of_last_tweet"] = d.strftime("%d %m %Y %H:%M:%S")
				return HttpResponseRedirect(reverse("twitter:home"))
			else:
				tweets = Tweet.objects.order_by("-published_on")[:5]
				return render(request,'twitter/home.html', 
					{"tweets":tweets, "user": request.user, 
					"f": f})
		else:
			f = TweetForm()
			tweets = Tweet.objects.order_by("-published_on")[:5]
			return render(request,'twitter/home.html', {"tweets":tweets,
			 	"user": request.user, 
				"f": f, "er30":error_tweet_30})
	else:
		f = TweetForm()
		tweets = Tweet.objects.order_by("-published_on")[:5]
		return render(request,'twitter/home.html', {"tweets":tweets,
		 	"user": request.user, 
			"f": f})

@no_login_please
def log_in(request):
	if request.POST:
		f = LoginForm(request.POST)
		if f.is_valid():
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				if request.GET.has_key("next"):
					redirect_path = request.GET["next"]
				else:
					redirect_path = reverse('twitter:home')
				return HttpResponseRedirect(redirect_path)
			else:
				return HttpResponseRedirect(reverse('twitter:login'))
		else:
			if request.GET.has_key("next"):
				context = {'next': request.GET["next"]}
			else:
				context = {}	
			context["f"] = f
			return render(request,'twitter/login.html', context)						
	else:
		if request.GET.has_key("next"):
			context = {'next': request.GET["next"]}
		else:
			context = {}
		f = LoginForm()
		context["f"] = f
		return render(request,'twitter/login.html', context)

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('twitter:login'))
	
@no_login_please
def registration(request):
	if request.user.is_anonymous():
		if request.POST:
			username = request.POST["username"]
			password = request.POST["password"]
			password2 = request.POST["password2"]
			email = request.POST["email"]

			u = User.objects.filter(username=username)
			if u:
				return render(request,'twitter/registration.html',
							{"error_message":"Choose another username"})

			u = User.objects.filter(email=email)

			if u:
				return render(request,'twitter/registration.html',
							{"error_message":"Choose another email"})	

			if (password!=password2):
				return render(request,'twitter/registration.html',
							{"error_message":"Passwords do not match"})	

			u = User.objects.create_user(username=username,
				email=email,password=password)
			u.save()
			return log_in(request)			

		else:
			return render(request,'twitter/registration.html')
	else:
		return HttpResponseRedirect(reverse('twitter:home'))


@login_required
def settings(request):
	if request.method == "POST":
		f = UserSettingsForm(request.POST)
		if f.is_valid():
			request.user.first_name = f.cleaned_data["first_name"]
			request.user.last_name = f.cleaned_data["last_name"]
			request.user.email = f.cleaned_data["email"]
			request.user.save()
			return HttpResponseRedirect(reverse("twitter:home"))
		else:
			return render(request,"twitter/settings.html",{"f":f})

	else:
		f = UserSettingsForm(instance=request.user)
		return render(request,"twitter/settings.html",{"f":f})