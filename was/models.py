# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

import xlwt
import xlrd
import datetime

@python_2_unicode_compatible
class User(models.Model):
    BEGINNER = 'beginner'
    NOVICE= 'novice'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    experienceChoices= (
    (BEGINNER, 'Beginner'),
    (NOVICE, 'Novice'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced'),
    )
    
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default='WeightAndSeeUser')
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    bodyWeight = models.IntegerField()
    userLevel = models.CharField(max_length=12,choices=experienceChoices,default=BEGINNER)
    squatMax = models.IntegerField(null=True)
    benchMax = models.IntegerField(null=True)
    deadliftMax = models.IntegerField(null=True)
    snatchMax = models.IntegerField(null=True)
    cleanMax = models.IntegerField(null=True)
    goals = models.CharField(max_length=240)
    
    def __str__(self):
        l = []
        l.append(self.userID)
        l.append(self.username)
        l.append(self.age)
        l.append(self.gender)
        l.append(self.bodyWeight)
        l.append(self.userLevel)
        l.append(self.squatMax)
        l.append(self.benchMax)
        l.append(self.deadliftMax)
        l.append(self.snatchMax)
        l.append(self.cleanMax)
        l.append(self.goals)
        return str(l)
    
    def mostRecentUser(self):
        users = list(User.objects.all())
        mostRecentUser = users[len(users)-1]
        return mostRecentUser #user object
        
    def excel(self):
        levelProg = {'beginner': 'phase0.xls', 'novice':'phase1.xls', 'intermediate':'phase2.xls', 'advanced':'phase3.xls'}
        myProg = levelProg[self.userLevel] ####how do you call user level
        
        workbook = xlrd.open_workbook('/home/stu/cadet08/x86249/IT394/WAS/weightandsee/was/'+myProg)
        sheet = workbook.sheet_by_index(0)

        data = []
        for i in range(0,1000):
            data.append(i)
        
        {row: None for row in data}

        for i in range(0,1000):
            try:
                data[i] = [sheet.cell_value(i, col) for col in range(sheet.ncols)]
            except IndexError:
                pass

        #attach maxes
        #data[2][2] = 475
        #data[3][2] = 330
        #data[4][2] = 557
        #also how do you do this
        if myProg != 'phase0.xls':
            data[2][2] = self.squatMax
            data[3][2] = self.benchMax
            data[4][2] = self.deadliftMax

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('test')

        for i in range (0,1000):
            try:
                for index, value in enumerate(data[i]):
                    sheet.write(i, index, value)
            except TypeError:
                pass
	    phase=myprog[0:6]
        output = self.username + '_' + str(phase) + '_' + str(datetime.date.today()) + '.xls'
	
        workbook.save('/home/stu/cadet08/x86249/IT394/WAS/weightandsee/was/workouts/'+output)
        
#@python_2_unicode_compatible
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
