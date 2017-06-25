#Dylan Myers
#ME492_A14

#the file sample_text was in a subfolder titled RW_Text_Files
filename = 'sample_text.txt'
fileLoc = 'RW_Text_Files'
filenameAct = fileLoc + '/' + filename

f = open(filenameAct, 'r')
all_lines = f.readlines()
f.close()

totalizer = 0
sumTotal = 0
numList = []

for line in all_lines:
	if line.startswith('X-DSPAM-Confidence:'):
		line = line.replace('X-DSPAM-Confidence:','')
		line = line.strip()
		line = float(line)
		numList.append(line)
		totalizer = totalizer +1
avgConf = sum(numList)/totalizer
print('The average spam confidence is ' + str(avgConf))
