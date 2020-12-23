from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

class Like(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    like = models.ManyToManyField(User)