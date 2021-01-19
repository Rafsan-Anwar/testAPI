from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, verbose_name='Phone')

class Like(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    like = models.ManyToManyField(User)

class Student(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    studentID = models.IntegerField()


class DetailedStudent(models.Model):
    BLOODGROUP =(
        ('A+', 'A(+ve)'),
        ('B+', 'B(+ve)'),
        ('O+', 'O(+ve)'),
        ('A-', 'A(-ve))'),
        ('B-', 'B(-ve)'),
        ('O-', 'O(-ve)'),
        ('AB+', 'AB(+ve)'),
        ('AB-', 'AB(-ve)'),
    )
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bloodGroup = models.CharField(max_length=3, choices=BLOODGROUP)
    address = models.CharField(max_length=1000)

class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentClass = models.IntegerField()

class Subject(models.Model):
    subject = models.CharField(max_length=255)
    student = models.ManyToManyField(Student)
