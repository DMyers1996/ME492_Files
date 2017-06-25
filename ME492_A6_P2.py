#Dylan Myers
#Assignment 6 prob 2

hoursWorked = float(raw_input('Enter the number of hours worked: '))
payRate = float(raw_input('Enter the pay rate per hour: $'))

if hoursWorked > 40:
	payAmount = ((hoursWorked - 40) * 1.5 + 40) * payRate
else:
	payAmount = hoursWorked * payRate
print ('Total amount earned: $' + str(payAmount))
