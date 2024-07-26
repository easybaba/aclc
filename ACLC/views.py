from django.shortcuts import render
from management.models import Member

def home(request):
    cData = Member.objects.all()
    cData = {
        'cData': cData
    }
    return render (request, "index.html", cData)

def about(request):
    return render (request,"about.html")

def services(request):
    return render (request,"service.html")