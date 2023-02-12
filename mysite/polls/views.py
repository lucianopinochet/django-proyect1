from django.http import HttpResponse
from django.shortcuts import render
from .models import *
def index(request):
    context = {'candidates': Candidate.objects.all()}
    return render(request,'polls/index.html',context)