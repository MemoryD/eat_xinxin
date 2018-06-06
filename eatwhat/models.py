#!python3
#-*- coding: utf_8 -*-

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50)

    school = models.ForeignKey(School)

    price = models.FloatField()

    location = models.CharField(max_length=100)

    category = models.ForeignKey(Category)

    comment = models.TextField()

    # grade = models.SmallIntegerField()

    def __str__(self):
        return self.name


# class User(models.Model):
#   name = models.CharField(max_length=30)

#   phone = models.CharField(max_length=11)

#   gender_list = ((1,'man'),(2,'female'))

#   gender = models.SmallIntegerField(choices=gender_list)

#   address = models.CharField(max_length=50)

#   def __str__(self):
#         return self.name


