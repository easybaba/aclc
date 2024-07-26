from django.urls import path
from . import views
from management import views

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('Contact-entry/', views.saveContact, name="contact-entry"),
    path('course-entry/', views.courseEntry, name="courseEntry"),
    path('saveCourseDetails/', views.saveCourseDetails, name="saveCourseDetails"),
    path('del-contact/<int:id>', views.delContact, name="delcontact"),
]