import re


with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    


times = [int(i) for i in re.findall(r"\d+", lines[0].split(":")[1])]
distances = [int(i) for i in re.findall(r"\d+", lines[1].split(":")[1])]


for t, d in zip(times, distances):
    