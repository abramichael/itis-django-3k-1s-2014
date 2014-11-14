from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from twitter.forms import LoginForm, AvatarUploadForm
from twitter.models import Tweet, Profile


def no_auth_please(v):
    def wrapper(request, *a, **k):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse("index"))
        else:
            return v(request, *a, **k)
    return wrapper

@login_required(login_url=reverse_lazy("sign_in"))
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("sign_in"))
    

@login_required(login_url=reverse_lazy("sign_in"))
def q(request):
    return HttpResponse("CLASSIFIED")

@login_required(login_url=reverse_lazy("sign_in"))
def index(request):
    return render(
        request, 
        "twitter/index.html",
        {
            "user": request.user.username,
            "tweets" : Tweet.objects.filter(user=request.user).order_by("-p_date")
        }
    )


def process(request):
    tweet = request.POST["tweet"]
    t = Tweet(
            text=tweet,
            p_date=timezone.now(),
            user=request.user
    )
    t.save()
    return HttpResponseRedirect(reverse('index'))

@no_auth_please
def sign_in(request):
    if request.POST:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = authenticate(
                                username=f.cleaned_data["username"],
                                password=f.cleaned_data["password"]
            )
            if user:
                login(request, user)
                if request.GET.has_key("next"):
                    return HttpResponseRedirect(request.GET["next"])
                else:
                    return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('sign_in'))
    else:
        f = LoginForm()
        context = {"f": f}
        if request.GET.has_key("next"):
            context["next"] = request.GET["next"]
        return render(request, "twitter/sign_in.html", context)


def edit_avatar(request):
    p = Profile.objects.filter(user=request.user)
    if request.method == 'POST':
        if p.exists():
            form = AvatarUploadForm(request.POST, request.FILES, instance=p[0])
        else:
            form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("index"))
    else:

        if p.exists():
            form = AvatarUploadForm(instance=p[0])
        else:
            form = AvatarUploadForm()
        return render(
            request,
            "twitter/edit_avatar.html",
            {
                "form" : form,
                'image' : p[0].avatar
            }
        )
