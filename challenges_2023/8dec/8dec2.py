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

steps = 0

r = re.compile(r"\w\wZ")

a = 'DVA'

while not re.match(r, a):
    for inst in instructions:
        a = tree[node.strip()][inst]
        steps +=1
        if re.match(r, a):
            print(a)
            break