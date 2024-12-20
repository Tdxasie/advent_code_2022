import math

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

first_col = []
second_col = {}
for line in lines:
    a, b = line.split('   ')
    a, b = int(a), int(b)
    first_col.append(a)
    if a not in second_col:
        second_col[a] = 0
    if b not in second_col:
        second_col[b] = 1
    else:
        second_col[b] += 1
    

tot = 0
for a in first_col:
    tot += a * second_col[a]
    
print(tot)