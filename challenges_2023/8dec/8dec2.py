import re
import sys

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()


instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]

tree = {}
for line in lines[2:]:
    node, paths = line.split('=')
    tree[node.strip()] = re.findall(r"\w+", paths)
    


current_nodes = list(filter(lambda n: re.match(r"\w\wA", n), tree.keys()))
print(current_nodes)

steps = 0

while True:
    for inst in instructions:
        for i, node in enumerate(current_nodes):
            current_nodes[i] = tree[node][inst]
        steps +=1
        if any([re.match(r"\w\wZ", i ) is not None for i in current_nodes]) and steps%100 == 0:
            print(current_nodes)
        if all([re.match(r"\w\wZ", i ) is not None for i in current_nodes]):
            print(steps)
            sys.exit(1)
