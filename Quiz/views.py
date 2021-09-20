from django.shortcuts import render,redirect
from .models import exam
from django.contrib import messages
# Create your views here.
def home(request):
    exams=exam.objects.all()
    return render(request,'Quiz/index.html',{'exams':exams})
def go(request):
    score=0
    ans_list=[]
    exams = exam.objects.all()
    for i in exams:
        a=request.POST[str(i.id)]
        if a==i.correct:
            score+=1
            messages.info(request,str(i.id)+") The answer is correct")
        else:
            score=score-0.2
            messages.info(request,str(i.id)+") The answer is wrong. Correct answer is "+i.correct)
    messages.info(request,"your Score is : "+str(score))
    return redirect('/')