

with open('6dec/input.txt') as infile:
	line = infile.readline()
for i in range(13, len(line)):
	if len(set(line[i-13:i+1])) == 14:
		print(i+1)
		break