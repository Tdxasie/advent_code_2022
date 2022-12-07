
import re 


with open("5dec/input.txt") as infile:
	lines = infile.read().splitlines()

stacks, instructions = lines[:lines.index('')][:-1], lines[lines.index(''):]
stacks = [[i for i in a] for a in stacks]
stacks = [[l[i] for i in range(1,35,4)] for l in stacks[::-1]]
stacks = [[l[i] for l in stacks if l[i] != ' '] for i in range(9)]

for inst in instructions[1:]:
	num, start, end = list(map(int,re.findall('\d+', inst)))
	stacks[end-1] += stacks[start-1][-num:]
	stacks[start-1] = stacks[start-1][:-num]

end = [l[-1] for l in stacks]
print(''.join(end))
