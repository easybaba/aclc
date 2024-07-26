from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  massage = models.TextField()

  def __str__(self):
        return self.firstname +" "+ self.lastname

class courseDetails(models.Model):
  courseName = models.CharField(max_length=255)
  duration = models.CharField(max_length=255)
  fee = models.IntegerField()
  avlSeats = models.IntegerField()
  remarks = models.TextField()

  def __str__(self):
        return self.courseName