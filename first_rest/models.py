
from tkinter import CASCADE
from venv import create
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()
    is_deleted = models.SmallIntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'stud11'
    

class College(models.Model):
    name = models.CharField(max_length=100)
    staff_count  = models.IntegerField()

   
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'college'




# Django signals....!
# generated token using django signal  -- token generated right after creating using users(student)
# from django.conf import settings
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance= None, created = False, **kwargs):
#     if created:
#         Token.objects.create(user= instance)   # one to one relationship with users

# @receiver(post_save, sender =Student)
# def say_hello(sender, instance= None, created= False, **kwargs):
#     if create:
#         print(f"Hello Good morning...!{instance.name}")

# @receiver(post_delete, sender = Student)
# def say_bye(sender, instance = None, created= False, **kwargs):
#            print(f"Bye Bye ...!{instance.name}")
