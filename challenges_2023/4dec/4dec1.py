import re

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    
    
tot = 0
for line in lines:
    _, pulls = line.split(':')
    win, have = pulls.split('|')
    win = re.findall(r'\d+', win)
    have = re.findall(r'\d+', have)
    count = len([i for i in win if i in have])
    tot += int(2**(count-1))

    
print(tot)