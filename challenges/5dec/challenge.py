
import re 

with open("input.txt") as infile:
	lines = infile.read().splitlines()

stacks, instructions = lines[:lines.index('')][:-1], lines[lines.index(''):]
stacks = [[i for i in a] for a in stacks]
stacks = [[l[i] for i in range(1,35,4)] for l in stacks[::-1]]
stacks = [[l[i] for l in stacks if l[i] != ' '] for i in range(9)]

for inst in instructions[1:]:
	num, start, end = list(map(int,re.findall('\d+', inst)))
	stacks[end-1] += stacks[start-1][-num:][::-1]
	stacks[start-1] = stacks[start-1][:-num]

end = [l[-1] for l in stacks]
print(''.join(end))


# stacks = [[i for i in a] for a in stacks]
# stacks = [[l[i] for i in range(1,35,4)] for l in [[i for i in a] for a in stacks][::-1]]
# stacks = [[l[i] for l in [[l[i] for i in range(1,35,4)] for l in [[i for i in a] for a in stacks][::-1]] if l[i] != ' '] for i in range(9)]


import re 


with open("input.txt") as infile:
	lines = infile.read().splitlines()

stacks, instructions = lines[:lines.index('')][:-1], lines[lines.index(''):]
stacks = [[i for i in a] for a in stacks]
stacks = [[l[i] for i in range(1,35,4)] for l in stacks[::-1]]
stacks = [[l[i] for l in stacks if l[i] != ' '] for i in range(9)]

# for inst in instructions[1:]:
# 	num, start, end = list(map(int,re.findall('\d+', inst)))
# 	stacks[end-1] += stacks[start-1][-num:][::-1]
# 	stacks[start-1] = stacks[start-1][:-num]

# [list(map(int,re.findall('\d+', inst)))for i in inst]
s = stacks
print([[[s[n[2]-1].append(s[n[1]-1].pop())for _ in range(n[0])] for [n] in [list(map(int,__import__('re').findall('\d+', i)))]] for i in instructions])

print(''.join([l[-1] for l in stacks]))




# for line in lines:
# 	print(re.findall("[A-Z]|\s{4}", line))
# s = lines
# print([i for l in s if(i:=__import__('re').findall("[A-Z]|\s{4}",l))!=[]][::-1])

# print([__import__('re').findall("[A-Z]|\s{4}",l) for l in s][::-1])

# [[x[i] for x in stacks if x[i] != ' '] for i in range(9)]


