from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from twitter.models import RawTweet

def index(request):
    return render(
        request, 
        "twitter/index.html",
        {
            "user": "Damir",
            "tweets" : RawTweet.objects.all().order_by("-p_date")
        }
    )
    
def process(request):
    tweet = request.POST["tweet"]
    t = RawTweet(text=tweet,
                 p_date=datetime.now()
        )
    t.save()
    return HttpResponseRedirect(reverse('index'))