import re

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

RED_LIM = 12
GREEN_LIM = 13
BLUE_LIM = 14

tot = 0
for line in lines:
    game, pulls = line.split(':')
    id = re.search(r"\d+", game).group(0)
    reds = re.findall(r"(\d+)\sred", pulls)
    blues = re.findall(r"(\d+)\sblue", pulls)
    greens = re.findall(r"(\d+)\sgreen", pulls)
    if any([int(i)>RED_LIM for i in reds]) or any([int(i)>BLUE_LIM for i in blues]) or any([int(i)>GREEN_LIM for i in greens]):
        continue
    tot += int(id)

print(tot)