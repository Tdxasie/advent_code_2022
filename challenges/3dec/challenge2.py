
with open("3dec/input.txt") as infile:
	lines = infile.read().splitlines()

tot = 0
for i in range(0, len(lines), 3):
	one = set(lines[i])
	two = set(lines[i+1])
	three = set(lines[i+2])
	l = ord([i for i in one if i in two and i in three][0])
	if l<91:
		tot+=l-38
	else:
		tot+=l-96
print(tot)