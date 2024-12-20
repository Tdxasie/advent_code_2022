import re

with open('input.txt', 'r') as infile:
    text = infile.read()

pattern = r"mul\((?P<X>\d{1,3}),(?P<Y>\d{1,3})\)"

regexp = re.compile(pattern)

muls = [m.groupdict() for m in regexp.finditer(text)]

tot = 0
for mul in muls:
    tot += int(mul['X'] ) * int(mul['Y'])
    
print(tot)