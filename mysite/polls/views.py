from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *
from django.urls import reverse
from django.db.models import F
from django.views import generic

def index(request):
    context = {'candidates': Candidate.objects.all()}
    return render(request,'polls/index.html',context)

class CandidateView(generic.DetailView):
    template_name = 'polls/candidate.html'
    model = Candidate

def vote(request):
    try:
        candidate = Candidate.objects.get(pk=request.POST['choice'])
        cname = candidate.name
    except KeyError:
        return render(request,'polls/index.html',{'error_message':"Didn't mark a candidate",'candidates': Candidate.objects.all()})
    else:
        candidate = Candidate.objects.filter(pk=request.POST['choice'])
        candidate.update(votes=F('votes') + 1) 
        return HttpResponseRedirect(reverse('polls:ty',args=[cname]))

def ty(request,candidate):
    return render(request,"polls/ty.html",{'candidate':candidate})