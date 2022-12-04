


with open('4dec/input.txt') as infile:
	lines = infile.read().splitlines()

num = 0
for line in lines:
	one, two = line.split(',')
	a,b = int(one.split('-')[0]), int(one.split('-')[1])
	c,d = int(two.split('-')[0]), int(two.split('-')[1])
	if a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d:
		num+=1

print(num)