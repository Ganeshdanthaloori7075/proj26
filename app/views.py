from django.shortcuts import render
from app.models import *

# Create your views here.


def tra(request):
    qsd=Trainers.objects.all()
    d={'tra':qsd}

    return render(request,'trainer.html',d)



def stu(request):
    asw=Students.objects.all()
    d={'stu':asw}

    return render(request,'student.html',d)
