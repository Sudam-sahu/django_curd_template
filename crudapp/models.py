from django.db import models



class StudentsData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    fee = models.IntegerField()
    assignment1 = models.IntegerField()
    assignment2 = models.IntegerField()
    assignment3 = models.IntegerField()
    assignment4 = models.IntegerField()

