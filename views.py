from polls.models import cricket
from polls.models import schedule
from django.http import HttpResponse
from django.template import loader
from polls.models import cricplayers
from .models import Question
from django.views import View

from django.utils.html import escape
def cbit(request):
       return render(request,'polls/indexs.html')
def cbitcric(request):
    x=schedule.objects.filter(game="cricket").all().order_by('dt')[::-1]
    c={'list':x}

    return render(request,'polls/cricket.html',c)

def cricket1(request,guess1,guess2):
    team1=cricket.objects.filter(psec=guess1).all()
    team2=cricket.objects.filter(psec=guess2).all()
    scores=cricplayers.objects.all()
    return render(request,'polls/cricket1.html',{'team1':team1,"team2":team2,'guess1':guess1,'guess2':guess2,'score':scores})

def cbitbas(request):
    x=schedule.objects.filter(game="basketball").all()
    c={'list':x}

    return render(request,'polls/Basketball.html',c)
def cbitkab(request):
    x=schedule.objects.filter(game="kabaddi").all()
    c={'list':x}

    return render(request,'polls/Kabaddi.html',c)
def cbitvol(request):
    x=schedule.objects.filter(game="volleyball").all()
    c={'list':x}

    return render(request,'polls/Volleyball.html',c)
