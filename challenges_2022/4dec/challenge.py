


# with open('4dec/input.txt') as infile:
# 	lines = infile.read().splitlines()

# num = 0
# for line in lines:
# 	one, two = line.split(',')
# 	a,b = int(one.split('-')[0]), int(one.split('-')[1])
# 	c,d = int(two.split('-')[0]), int(two.split('-')[1])
# 	if a<=c<=b and a<=d<=b or c<=a<=d and c<=b<=d:
# 		num+=1

# print(num)

# print(map(lambda l: l.split(','), lines))
print(sum([int(x[0][0]<=x[1][0]<=x[0][1] and x[0][0]<=x[1][1]<=x[0][1] or x[1][0]<=x[0][0]<=x[1][1] and x[1][0]<=x[0][1]<=x[1][1])for x in [[list(map(int,i.split('-')))for i in l.split(',')]for l in open('4dec/input.txt').read().splitlines()]]))


print(sum([int(x[0]<=y[0]<=x[1]and x[0]<=y[1]<=x[1]or y[0]<=x[0]<=y[1]and y[0]<=x[1]<=y[1])for x,y in [[list(map(int,i.split('-')))for i in l.split(',')]for l in open('v').read().splitlines()]]))

# chal1 
print(sum([a<=c<=b and a<=d<=b or c<=a<=d and c<=b<=d for (a,b),(c,d)in [[list(map(int,i.split('-')))for i in l.split(',')]for l in open('v').read().splitlines()]]))

# chal2
print(sum([a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d for (a,b),(c,d)in [[list(map(int,i.split('-')))for i in l.split(',')]for l in open('v').read().splitlines()]]))
