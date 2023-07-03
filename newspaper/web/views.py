from django.shortcuts import render
from web.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

"""
def login_view(request):
    if request.method == "GET":
        return render(request, "web/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse("web:index"))
        else:
            # Return an 'invalid login' error message.
            return render(request, "web/login.html", {"Error": "Login did not process through. Please try Again."})


# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, "web/index.html", {"posts": Article.objects.all()[0:5]})

"""

#@login_required(login_url='/login')
def article_view(request, articleID):
    if request.method == "GET":
        #return render(request, "web/new_layout.html", {"site": Article.objects.get(article_id=articleID), "posts": Article.objects.all()[0:5]})
        #us = request.api_key
        return JsonResponse({"site": Article.objects.get(article_id=articleID), "posts": Article.objects.all()[0:5]})