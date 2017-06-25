#Dylan Myers
#ME492_HW3_P3

from numpy import *

def roots(a,b,c):
	if b**2.0-4.0*a*c >= 0:
		root1 = (-b+sqrt(b**2.0-4.0*a*c))/(2.0*a)
		root2 = (-b-sqrt(b**2.0-4.0*a*c))/(2.0*a)
		print('Root 1: ' + str(root1) + '\n' + 'Root 2: ' + str(root2))
	else:
		print('Error: The roots are complex')
