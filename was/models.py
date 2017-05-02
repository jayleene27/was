# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

import xlwt
import xlrd
import datetime

@python_2_unicode_compatible
class User(models.Model):
    '''BEGINNER = 'beginner'
    NOVICE= 'novice'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    experienceChoices= (
    (BEGINNER, 'Beginner'),
    (NOVICE, 'Novice'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced'),
    )'''
    
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, default='WeightAndSeeUser')
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    bodyWeight = models.IntegerField()
    #userLevel = models.CharField(max_length=12,choices=experienceChoices,default=BEGINNER)
    squatMax = models.IntegerField(null=True)
    benchMax = models.IntegerField(null=True)
    deadliftMax = models.IntegerField(null=True)
        
    def __str__(self):
        l = []
        l.append(self.userID)
        l.append(self.username)
        l.append(self.age)
        l.append(self.gender)
        l.append(self.bodyWeight)
        #l.append(self.userLevel)
        l.append(self.squatMax)
        l.append(self.benchMax)
        l.append(self.deadliftMax)
        l.append(self.total)
        return str(l)
    
    def mostRecentUser(self):
        users = list(User.objects.all())
        mostRecentUser = users[len(users)-1]
        return mostRecentUser #user object
    
    def levelPicker(self,bw,gen):
        total=self.deadliftMax+self.benchMax+self.squatMax
        levels = ['advanced','intermediate','novice','beginner']    
    #establish standards based on gender
        if gen == 'F':
            weightClasses = [97,105,114,123,132,148,165,181,198,999]
            totals = {97:[362,417,466],105:[392,446,506],114:[421,482,541],123:[446,511,575],132:[472,541,605],148:[521,595,670],165:[561,635,725],181:[605,689,779],198:[635,739,828],999:[680,779,873]}
        if gen == 'M':
            weightClasses = [114,123,132,148,165,181,198,220,242,275,308,999]
            totals = {114:[605,699,794],123:[660,754,858],132:[709,841,923],148:[798,908,1037],165:[869,992,1131],181:[932,1071,1215],198:[987,1131,1280],220:[1041,1191,1355],242:[1076,1230,1399],308:[1151,1325,1503],999:[1186,1365,1548]}

        #determine weight class 
        while bw > weightClasses[0]:
            weightClasses.pop(0)
            if len(weightClasses)== 1:
                break
            
        #determine what the highest total underneath which the user's total falls
        while total > totals[weightClasses[0]][0]: 
            totals[weightClasses[0]].pop(0)
            if len(totals[weightClasses[0]]) == 0:
                break
                
        #determine skill level based on how many totals from list are left
        level = levels[len(totals[weightClasses[0]])]
        
        return level
    
    def excel(self,userLevel):
        levelProg = {'beginner': 'phase0.xls', 'novice':'phase1.xls', 'intermediate':'phase2.xls', 'advanced':'phase3.xls'}
        myProg = levelProg[userLevel] ####how do you call user level
        
        workbook = xlrd.open_workbook(r'/home/stu/cadet08/x86249/IT394/WAS/weightandsee/was/'+myProg)
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
        sheet = workbook.add_sheet('Schedule')

        for i in range (0,1000):
            try:
                for index, value in enumerate(data[i]):
                    sheet.write(i, index, value)
            except TypeError:
                print('')
        
        phase = myProg[0:6]
	    
        output = self.username + '_' + str(phase) + '_' + str(datetime.date.today()) + '.xls'
	
        workbook.save(r'/home/stu/cadet08/x86249/IT394/WAS/workouts/'+output)
        
#@python_2_unicode_compatible
'''class Exercises(models.Model):
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
    exMax = models.IntegerField()'''
