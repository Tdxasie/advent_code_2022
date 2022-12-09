

with open('9dec/input.txt') as infile:
	lines = infile.read().splitlines()

for line in lines:
	command = line[0]
	distance = int(line[2])
	print(distance)
	match command:
		case 'L':
			# go left
			pass
		case 'R':
			# go right
			pass
		case 'U':
			# go up 
			pass
		case 'D':
			# go down
			pass