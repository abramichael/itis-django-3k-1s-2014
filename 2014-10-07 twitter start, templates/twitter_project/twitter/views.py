from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(
		request, 
		"twitter/index.html",
		{"user": "Shagit",
		 "tweets" : [] #["Hi!", "Good bye!"]
		}	
	)
	
def process(request):
    tweet = request.POST["tweet"]
    print "GOT: " + tweet
    return HttpResponseRedirect("/")