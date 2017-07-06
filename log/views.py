#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"demo.html")

def about(request):
	return render(request,"about.html")

def postdata(request):
	return render(request,"home.html")
