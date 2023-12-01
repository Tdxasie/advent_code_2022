import functools


# with open('input.txt') as infile:
#     lines = infile.read().splitlines()

# score = 0
# for line in lines:
#     l = line.split(' ')
#     score += -(23-(ord(l[1])-64))
#     if ord(l[0])-64== -(23-(ord(l[1])-64)):
#         score += 3
#         continue
#     if l[0] == 'C' and l[1] == 'X' or l[0] == 'A' and l[1] == 'Y' or l[0] == 'B' and l[1] == 'Z':
#         score += 6


# print(score)

# score += -(23-ord(l[1])-64)




# with open('input.txt') as infile:
#     lines = infile.read().splitlines()


# mat = [[3,0,6],[6,3,0],[0,6,3]]
# score = 0
# for line in lines:
#     score += -(23-(ord(line.split(' ')[1])-64)) + [[3,0,6],[6,3,0],[0,6,3]][-(23-(ord(line.split(' ')[1])-64))-1][ord(line.split(' ')[0])-64-1]
    

# print(score)

# print(functools.reduce(lambda score, l: score + (-(23-(ord(l.split(' ')[1])-64)) + [[3,0,6],[6,3,0],[0,6,3]][-(23-(ord(l.split(' ')[1])-64))-1][ord(l.split(' ')[0])-64-1]),lines))

print(sum([-(23-(ord(l.split(' ')[1])-64)) + [[3,0,6],[6,3,0],[0,6,3]][-(23-(ord(l.split(' ')[1])-64))-1][ord(l.split(' ')[0])-65] for l in open('input.txt').read().splitlines()]))

# 17189

# score += -(23-ord(l[1])-64)d