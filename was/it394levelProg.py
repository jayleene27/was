import xlwt
import xlrd
import datetime
from was.models import User

levelProg = {'beginner': 'phase0.xls', 'novice':'phase1.xls', 'intermediate':'phase2.xls', 'advanced':'phase3.xls'}
myProg = levelProg[self.User.userLevel()] ####how do you call user level

workbook = xlrd.open_workbook(myProg)
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
data[2][2] = self.User.squatMax()
data[3][2] = self.User.benchMax()
data[4][2] = self.User.deadliftMax()

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for i in range (0,1000):
    try:
        for index, value in enumerate(data[i]):
            sheet.write(i, index, value)
    except TypeError:
        pass
	
#also how do you do this
output = self.User.username() + str(datetime.date.today()) + '.xls'
	
workbook.save(output)
