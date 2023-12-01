


with open('input.txt') as infile:
    lines = infile.read().splitlines()

score = 0
for line in lines:
    l = line.split(' ')
    if l[1] == 'X': # lose
        if l[0] == 'A':
            score += 3
        if l[0] == 'B':
            score += 1
        if l[0] == 'C':
            score += 2
    elif l[1] == 'Y': # draw
        if l[0] == 'A':
            score += 1
        if l[0] == 'B':
            score += 2
        if l[0] == 'C':
            score += 3
        score += 3
    elif l[1] == 'Z': # win
        if l[0] == 'A':
            score += 2
        if l[0] == 'B':
            score += 3
        if l[0] == 'C':
            score += 1
        score += 6

print(score)

# score += -(23-ord(l[1])-64)