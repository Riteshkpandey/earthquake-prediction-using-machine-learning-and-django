from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

# from django.http.response import HttpResponse

# Create your views here.
def home(req):
    return render(req,"homepage.html")
def about(req):
    return render(req,"about.html")

def contactus(req):
    return render(req,"contactus.html")
