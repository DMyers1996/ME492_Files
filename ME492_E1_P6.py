#Dylan Myers
#ME492_E1_P6

from numpy import *

def report_card():
	classesTaken = int(raw_input('How many classes did you take? '))
	classNames = []
	classGrades = []
	totalPoints = 0
	for i in arange(classesTaken):
		classNames.append(raw_input('What was the name of this class? '))
		classGrades.append(raw_input('What was your grade? '))
	for i in arange(classesTaken):
		totalPoints = totalPoints + int(classGrades[i])
	finalGPA = float(totalPoints)/classesTaken
	print '\nREPORT CARD:'
	for i in arange(classesTaken):
		print(classNames[i] + ' - ' + classGrades[i])
	print('Overall GPA - ' + str(finalGPA))
