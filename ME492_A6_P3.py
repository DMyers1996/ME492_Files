#Dylan Myers
#Assignment 6 prob 3

#Guess: The script will ask for a number and convert it to an integer.
#		The script will then check to see if the number is divisible
#		by any positive integer smaller than itself, except for 1.
#		The program will print any number which is only divisible 
#		by itself and 1. The result will be a list of prime integers
#		which are less than the number entered.

N = input("Please enter a number as an upper limit:")
N = int(N)
for i in range(2,N):
	check_var = True
	for k in range(2,i):
		if (i%k) == 0:
			check_var = False
	if check_var:
		print(i)
