from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# School activities class
class School_Activities(models.Model):
    # Relation to user model will be used display user specific data. Data only by the auth user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    # return activity name
    def __str__(self):
        return self.name


# class students
class Students(models.Model):
    # Relation to user model will be used to display user specific data. Data only by the auth user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    student_ID = models.CharField(max_length=200, unique=True)
    activity = models.ForeignKey(School_Activities, related_name="activities", blank=True, on_delete=models.PROTECT)

    # return student first and second name
    def __str__(self):
        return f"{self.first_name} {self.second_name}"

