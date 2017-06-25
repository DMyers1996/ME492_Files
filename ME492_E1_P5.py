#Dylan Myers
#ME492_E1_P5

def quest5(xVal, coefList):
	coefListRev = list(reversed(coefList))
	totalizer = 0
	for i, coefn in enumerate(coefListRev):
		totalizer = coefn*xVal**i + totalizer
	return totalizer

val1 = 2
val2 = [1,2,3,4]

answer1 = quest5(val1,val2)
print answer1
