def levelPicker(total,bw,gen):
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
    
    print(level)
    
levels = ['advanced','intermediate','novice','beginner']

#tests

levelPicker(600,130,'F')
levelPicker(1355,180,'M')
levelPicker(300,92,'F')
levelPicker(1300,350,'M')


def meetAttemps(squatMax,benchMax,deadliftMax):
    ################################################     SQUAT     ############################################
    
    squatFeel = int(input('On a scale of 0 to 10, how are you feeling on the squat? (10 being great, 0 being terrible)'))
    squatDif = .005 * (-1 * (5 - squatFeel))  
    squatPerc = (.9+squatDif)
    squat1 = squatPerc*squatMax
    
    
    print('First squat: ' + str(squat1))
    
    #second squat attempt
    hitOrMiss = input('Did you hit or miss your first squat? ')
    if hitOrMiss == 'hit':
        
        squatFeel = int(input('On a scale of 1 to 10, how did you feel for the 1st squat? (10 being ridiculously easy, 1 being terribly difficult) '))
        squatDif = .0075*squatFeel
        squatPerc = squatPerc+squatDif
        squat2 = squatPerc*squatMax
        
        if squat2 < (squat1 + 5):
            squat2 = (squat1 + 5)
            
        
    elif hitOrMiss == 'miss':
        squat2 = squat1
    
    print(('Second squat: ' + str(squat2)))
    
    #last squat attempt
    hitOrMiss = input('Did you hit or miss your second squat? ')
    if hitOrMiss == 'hit':
        
        squatFeel = int(input('On a scale of 1 to 10, how did you feel for the 2nd squat? (10 being ridiculously easy, 1 being terribly difficult) '))
        squatDif = .0075*squatFeel
        squatPerc = squatPerc+squatDif
        squat3 = squatPerc*squatMax
        
        if squat3 < (squat2 + 5):
            squat3 = (squat2 + 5)
            
        
    elif hitOrMiss == 'miss':
        squat3 = squat2
    
    print(('Final squat: ' + str(squat3)))
    
    ################################################     bench     ############################################
    
    benchFeel = int(input('On a scale of 0 to 10, how are you feeling on the bench? (10 being great, 0 being terrible)'))
    benchDif = .005 * (-1 * (5 - benchFeel))  
    benchPerc = (.9+benchDif)
    bench1 = benchPerc*benchMax
    
    
    print('First bench: ' + str(bench1))
    
    #second bench attempt
    hitOrMiss = input('Did you hit or miss your first bench? ')
    if hitOrMiss == 'hit':
        
        benchFeel = int(input('On a scale of 1 to 10, how did you feel for the 1st bench? (10 being ridiculously easy, 1 being terribly difficult) '))
        benchDif = .0075*benchFeel
        benchPerc = benchPerc+benchDif
        bench2 = benchPerc*benchMax
        
        if bench2 < (bench1 + 5):
            bench2 = (bench1 + 5)
            
        
    elif hitOrMiss == 'miss':
        bench2 = bench1
    
    print(('Second bench: ' + str(bench2)))
    
    #last bench attempt
    hitOrMiss = input('Did you hit or miss your second bench? ')
    if hitOrMiss == 'hit':
        
        benchFeel = int(input('On a scale of 1 to 10, how did you feel for the 2nd bench? (10 being ridiculously easy, 1 being terribly difficult) '))
        benchDif = .0075*benchFeel
        benchPerc = benchPerc+benchDif
        bench3 = benchPerc*benchMax
        
        if bench3 < (bench2 + 5):
            bench3 = (bench2 + 5)
            
        
    elif hitOrMiss == 'miss':
        bench3 = bench2
    
    print(('Final bench: ' + str(bench3)))
    
    ################################################     deadlift     ############################################
    
    deadliftFeel = int(input('On a scale of 0 to 10, how are you feeling on the deadlift? (10 being great, 0 being terrible)'))
    deadliftDif = .005 * (-1 * (5 - deadliftFeel))  
    deadliftPerc = (.9+deadliftDif)
    deadlift1 = deadliftPerc*deadliftMax
    
    
    print('First deadlift: ' + str(deadlift1))
    
    #second deadlift attempt
    hitOrMiss = input('Did you hit or miss your first deadlift? ')
    if hitOrMiss == 'hit':
        
        deadliftFeel = int(input('On a scale of 1 to 10, how did you feel for the 1st deadlift? (10 being ridiculously easy, 1 being terribly difficult) '))
        deadliftDif = .0075*deadliftFeel
        deadliftPerc = deadliftPerc+deadliftDif
        deadlift2 = deadliftPerc*deadliftMax
        
        if deadlift2 < (deadlift1 + 5):
            deadlift2 = (deadlift1 + 5)
            
        
    elif hitOrMiss == 'miss':
        deadlift2 = deadlift1
    
    print(('Second deadlift: ' + str(deadlift2)))
    
    #last deadlift attempt
    hitOrMiss = input('Did you hit or miss your second deadlift? ')
    if hitOrMiss == 'hit':
        
        deadliftFeel = int(input('On a scale of 1 to 10, how did you feel for the 2nd deadlift? (10 being ridiculously easy, 1 being terribly difficult) '))
        deadliftDif = .0075*deadliftFeel
        deadliftPerc = deadliftPerc+deadliftDif
        deadlift3 = deadliftPerc*deadliftMax
        
        if deadlift3 < (deadlift2 + 5):
            deadlift3 = (deadlift2 + 5)
            
        
    elif hitOrMiss == 'miss':
        deadlift3 = deadlift2
    
    print(('Final deadlift: ' + str(deadlift3)))

#test
#meetAttemps(480,330,550)
