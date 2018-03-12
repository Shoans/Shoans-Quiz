from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request,'home.html')


class LoginView(TemplateView):
    template_name = 'register/login.html'


def login(request):
    return HttpResponseRedirect('/login')