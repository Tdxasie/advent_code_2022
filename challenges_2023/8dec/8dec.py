import re

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()


instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]

tree = {}
for line in lines[2:]:
    node, paths = line.split('=')
    tree[node.strip()] = re.findall(r"\w+", paths)
    
current = 'AAA'
steps = 0
while current != 'ZZZ':
    for inst in instructions:
        current = tree[current][inst]
        steps += 1
        if current == 'ZZZ':
            break

print(steps)
