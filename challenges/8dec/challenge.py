import numpy as np

with open('8dec/input.txt') as infile:
	lines = infile.read().splitlines()

lines = np.array([[[int(i),False] for i in l] for l in lines])

l,h,d = lines.shape

for i in range(1,l-1):
	col = lines[:, i]
	maxcol = max(col[:, 0])
	max_seen = col[0][0]
	col[0][1] = True
	for t in col[1:]:
		if t[0] > max_seen:
			max_seen = t[0]
			t[1] = True if not t[1] else t[1]
			if t[0] == maxcol:
				break

for i in range(1,l-1):
	col = lines[:, i]
	maxcol = max(col[:, 0])
	col = col[::-1]
	max_seen = col[0][0]
	col[0][1] = True
	for t in col[1:]:
		if t[0] > max_seen:
			max_seen = t[0]
			t[1] = True if not t[1] else t[1]
			if t[0] == maxcol:
				break

for i in range(1,l-1):
	col = lines[i, :]
	maxcol = max(col[:, 0])
	max_seen = col[0][0]
	col[0][1] = True
	for t in col[1:]:
		if t[0] > max_seen:
			max_seen = t[0]
			t[1] = True if not t[1] else t[1]
			if t[0] == maxcol:
				break

for i in range(1,l-1):
	col = lines[i, :]
	maxcol = max(col[:, 0])
	col = col[::-1]
	max_seen = col[0][0]
	col[0][1] = True
	for t in col[1:]:
		if t[0] > max_seen:
			max_seen = t[0]
			t[1] = True if not t[1] else t[1]
			if t[0] == maxcol:
				break

a = [[j[1] for j in i] for i in lines]
a = sum([item for sublist in a for item in sublist])
print(a+4)


