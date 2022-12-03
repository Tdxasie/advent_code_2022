
with open("input.txt") as infile:
	lines = infile.read().splitlines()

tot = 0
for line in lines:
	mid = int(len(line)/2)
	one, two = set(line[:mid]), set(line[mid:])
	l = ord([i for i in one if i in two][0])
	if l<91:
		tot+=l-38
	else:
		tot+=l-96
print(tot)

# with open("3dec/input.txt") as infile:
# 	lines = infile.read().splitlines()

# tot = 0
# for line in lines:
# 	l = ord([i for i in set(line[:int(len(line)/2)]) if i in set(line[int(len(line)/2):])][0])
# 	tot += l-38 if l<91 else l-96
# print(tot)

print(sum([[lambda:b-96,lambda:b-38][b<91]() for b in [ord([i for i in set(l[:int(len(l)/2)]) if i in set(l[int(len(l)/2):])][0]) for l in open('v').read().splitlines()]]))
