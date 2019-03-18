from django.shortcuts import render,redirect
from .forms import Questions,Choices
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import User
from .models import Questions

# Create your views here.

@login_required(login_url="/auth/login")
def home(request):
    qForm = Questions()
    return render(request,"index.html",{"qform":qForm})

def createquestionnaire(request):
    qForm = Questions()
    cForm = Choices()
    if request.method == 'POST':
        qForm = Questions(request.POST)
        cForm = Choices(request.POST)
        if qForm.is_valid() and cForm.is_valid():
            question = qForm.save(commit=False)
            choices = cForm.save(commit=False)
            question.save()
            question.user = request.user
            choices.Questions = question
            choices.save()
            return redirect("/")
        # return render(request,"create.html",{"qform":qForm,"cform":cForm})
    return render(request,"create.html",{"qform":qForm,"cform":cForm})

def filling(request,username):
    asker = User.objects.get(username=username)
    questions = Questions.objects.filter(user=asker)
    return render(request,"answer.html",{"questions":questions})

