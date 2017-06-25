#Dylan Myers
#ME492_HW3_P4

def pig_latin(word):
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	word = word.strip()
	if word[0] in vowels:
		word = word + 'hay'
	else:
		word = word[1:] + word[0] + 'ay'
	print word
