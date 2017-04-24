# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default='WeightAndSeeUser')
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    bodyWeight = models.IntegerField()
    squatMax = models.IntegerField(null=True)
    benchMax = models.IntegerField(null=True)
    deadliftMax = models.IntegerField(null=True)
    snatchMax = models.IntegerField(null=True)
    cleanMax = models.IntegerField(null=True)
    goals = models.CharField(max_length=240)
    def __str__(self):
        attr=['userID',
        'username',
        'age',
        'gender',
        'bodyWeight',
        'squatMax',
        'benchMax',
        'deadliftMax',
        'snatchMax',
        'cleanMax',
        'goals']
        l = []
        l.append(self.userID)
        l.append(self.username)
        l.append(self.age)
        l.append(self.gender)
        l.append(self.bodyWeight)
        l.append(self.goals)
        return str(l)
    
@python_2_unicode_compatible
class Exercises(models.Model):
    exID = models.AutoField(primary_key=True)
    orderNum = models.IntegerField()
    purpose = models.CharField(max_length=240)
    main = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    alt1 = models.CharField(max_length=30)
    alt2 = models.CharField(max_length=30)
    alt3 = models.CharField(max_length=30)
    
class UserDoesExercise(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    phase = models.IntegerField()
    date = models.DateField()
    exMax = models.IntegerField()