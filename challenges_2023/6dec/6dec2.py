import re
import numpy as np
from math import floor

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    


times = [int(i) for i in re.findall(r"\d+", lines[0].split(":")[1])]
distances = [int(i) for i in re.findall(r"\d+", lines[1].split(":")[1])]

t = int(f"{times[0]}{times[1]}{times[2]}{times[3]}")
d = int(f"{distances[0]}{distances[1]}{distances[2]}{distances[3]}")

roots = sorted(np.roots([-1, (t), -1*(d+0.5)]))
vals = floor(roots[1]) - floor(roots[0])
    
print(vals)