#Dylan Myers
#ME492_HW2_P3

print '\nProgrammed by Dylan Myers\n'
aCoef = int(raw_input('Enter the first number: '))
bCoef = int(raw_input('Enter the second number: '))
cCoef = int(raw_input('Enter the third number: '))
numGoal = int(raw_input('Enter the final total: '))

iCnt = 0
found = False

while aCoef*iCnt <= numGoal and found == False:
	jCnt = 0
	while aCoef*iCnt+bCoef*jCnt <= numGoal and found == False:
		kCnt = 0
		while aCoef*iCnt+bCoef*jCnt+cCoef*kCnt <= numGoal and found == False:
			num = aCoef*iCnt+bCoef*jCnt+cCoef*kCnt
			if num == numGoal:
				found = True
			kCnt = kCnt + 1
		jCnt = jCnt + 1
	iCnt = iCnt + 1
if found == True:
	print('\nThe answers are:')
	print('\t' + str(iCnt-1) + ' of the first number, ' + str(aCoef))
	print('\t' + str(jCnt-1) + ' of the second number, ' + str(bCoef))
	print('\t' + str(kCnt-1) + ' of the third number, ' + str(cCoef))
else:
	print('\nNo such solution exists')
