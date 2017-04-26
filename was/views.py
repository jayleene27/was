# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from was.models import User
from .forms import RegisterForm

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form.save()
        return HttpResponseRedirect('/was/submitted')
    else:
        form=RegisterForm().as_p()
    return render(request, 'register.html',{'form': form})

def submitted(request):
    user=User()
    user.excel()
    template = loader.get_template('submitted.html')
    #return HttpResponse(template.render(request))
    return render(request, 'submitted.html')
