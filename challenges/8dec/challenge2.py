import numpy as np

with open('8dec/input.txt') as infile:
	lines = infile.read().splitlines()

lines = np.array([[int(i) for i in l] for l in lines])

l,h = lines.shape

scores = np.zeros((l,h))

def count_trees(tree, dir):
    count = 0
    for t in dir:
        count+=1
        if t>=tree:
            break
    return count

# print(lines)
max_view = 0
for i in range(l):  # lines 
    for j in range(h):  # cols 
        count = 1
        tree = lines[i][j]

        up = lines[:i, j][::-1]
        if up.any():
            count *= count_trees(tree, up)
        else:
            continue

        down = lines[i+1:, j]
        if down.any():
            count *= count_trees(tree, down)
        else:
            continue
        
        left = lines[i, j+1:]
        if left.any():
            count *= count_trees(tree, left)
        else:
            continue

        right = lines[i, :j][::-1]
        if right.any():
            count *= count_trees(tree, right)
        else:
            continue
        
        scores[i][j] = count
        
        max_view = max(count, max_view)

print(max_view)


