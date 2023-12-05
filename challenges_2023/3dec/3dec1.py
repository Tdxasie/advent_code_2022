import re

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

def is_symbol(char):
    symbols = [re.findall(r"(\D)", line) for line in lines]
    symbols = [[i for i in a if i != '.'] for a in symbols]
    symbols = set([item for sublist in symbols for item in sublist])
    return char in symbols

def get_line(line: str):
    global count
    line = re.findall(r"(\d+|\D)", line)
    result = []
    for match in line:
        if match.isdigit():
            count += 1
            result.extend([match] * len(match))
        else:
            result.append(match)
    return result


grid = [get_line(line) for line in lines]



for x, row in enumerate(grid):
    for y, col in enumerate(row):
        a = grid[x][y]
        if a.isdigit():
            ...

