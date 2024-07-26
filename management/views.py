from django.shortcuts import render, HttpResponseRedirect, redirect
from management.models import Member, courseDetails
from django.contrib.sessions.backends.db import SessionStore
from django.urls import reverse


# Create your views here. 
def contact(request):
    return render(request,"contact.html")

def saveContact(request):
    n = ""
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        massage = request.POST['subject']
        mData = Member(firstname=firstname, lastname=lastname, massage=massage)
        mData.save()
        n = "Data Inserted"
        return HttpResponseRedirect(reverse('contact'),{'n': n})
    else:
        return render(request, "contact.html", {'n': n})
    
def delContact(request, id):
  member = Member.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('Home'))

def courseEntry(request):
    return render (request,"courseEntry.html")

def saveCourseDetails(request):
    if request.method == "POST":
        course_name = request.POST['coursename']
        course_duration = request.POST['duration']
        course_fee = int(request.POST['fee'])
        avl_seats = int(request.POST['avlseats'])
        course_description = request.POST['remarks']
        
        courseData = courseDetails(
            courseName=course_name,
            duration=course_duration,
            fee=course_fee,
            avlSeats=avl_seats,
            remarks=course_description
        )
        courseData.save()
        
        return HttpResponseRedirect(reverse("Home"), {'n': "Course Details Saved Successfully"})

    return HttpResponseRedirect(reverse("Home"))