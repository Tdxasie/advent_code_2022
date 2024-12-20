import re

with open('input.txt', 'r') as infile:
    text = infile.read()

mulpat = r"mul\((?P<X>\d{1,3}),(?P<Y>\d{1,3})\)"
dontpat = r"don't\(\)(.|\n)*?do\(\)"

mulex = re.compile(mulpat)

text = re.sub(dontpat, " ", text)

muls = [m.groupdict() for m in mulex.finditer(text)]

tot = 0
for mul in muls:
    tot += int(mul['X'] ) * int(mul['Y'])
    
print(tot)