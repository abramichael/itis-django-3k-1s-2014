from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView

from twitter.forms import LoginForm
from twitter.models import Tweet

class UserTweetListView(ListView):
    model = Tweet
    template_name = "twitter/index.html"
    context_object_name = "tweets"
    paginate_by = 3

    def get_queryset(self):
        qs = Tweet.objects.filter(user_id=self.request.user.id).order_by("-p_date")
        return qs

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserTweetListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserTweetListView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().values_list("id", "username")
        return context

class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy("index")
    template_name = "twitter/sign_in.html"

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user:
            login(self.request, user)
            if self.request.GET.has_key("next"):
                return redirect(self.request.GET["next"])
            else:
                return redirect(reverse_lazy('index'))
        else:
            return redirect(reverse_lazy('sign_in'))

def no_auth_please(v):
    def wrapper(request, *a, **k):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse("index"))
        else:
            return v(request, *a, **k)
    return wrapper

@login_required
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
