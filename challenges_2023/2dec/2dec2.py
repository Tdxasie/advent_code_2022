import re

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

tot = 0
for line in lines:
    game, pulls = line.split(':')
    id = re.search(r"\d+", game).group(0)
    reds = max([int(i) for i in re.findall(r"(\d+)\sred", pulls)])
    blues = max([int(i) for i in re.findall(r"(\d+)\sblue", pulls)])
    greens = max([int(i) for i in re.findall(r"(\d+)\sgreen", pulls)])
    tot += reds * blues * greens 

print(tot)