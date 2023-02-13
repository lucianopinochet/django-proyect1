from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *
from django.urls import reverse

def index(request):
    context = {'candidates': Candidate.objects.all()}
    return render(request,'polls/index.html',context)

def candidate_info(request, candidate_name):
    try:
        context = {'candidate': get_object_or_404(Candidate,name=candidate_name)}
    except Candidate.DoesNotExist:
        raise Http404("Candidate does not exist.")
    return render(request, 'polls/candidate.html',context)

def vote(request):
    if request.method == 'GET':
        context = {'candidates': Candidate.objects.all()}
        return render(request,'polls/index.html',context)
    
    try:
        candidate = Candidate.objects.get(pk=request.POST['choice'])
    except KeyError:
        return render(request,'polls/index.html',{'error_message':"Didn't mark a candidate",'candidates': Candidate.objects.all()})
    else:
        candidate.votes += 1
        candidate.save()
        print(candidate.name)
        return HttpResponseRedirect(reverse('polls:ty',args=[candidate.name]))

def ty(request,candidate):
    return render(request,"polls/ty.html",{'candidate':candidate})