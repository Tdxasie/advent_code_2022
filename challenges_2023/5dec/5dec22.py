import re
from typing import Any
from numpy import interp
from functools import partial
from dataclasses import dataclass

@dataclass
class Mup:
    range: range
    map: callable


class Map:
    def __init__(self, maps):
        self.maps = []
        for map in maps:
            if map == []:
                continue
            self.update_map(map)
            
    def update_map(self, map):
        target_start, source_start, length = map
        def mapf(val):
            return int(interp(val, [source_start, source_start+length], [target_start, target_start+length]))
        self.maps.append(Mup(range(source_start, source_start+length), mapf))
        
            
    def __call__(self, val):
        for map in self.maps:
            if val in map.range:
                return map.map(val)
        return val
                
with open('input.txt', 'r') as infile:
    lines = infile.read()
    
lines = lines.split(":")
seeds = [int(i) for i in re.findall(r'\d+', lines[1])]
maps = [Map([[int(j) for j in re.findall(r'\d+', a)] for a in i.split('\n\n')[0].split('\n')]) for i in lines[2:]]

ranges = [seeds[n:n+2] for n in range(0, len(seeds), 2)]

vals = []
for range_ in ranges:
    a = []
    for boundary in range_:
        for map in maps:
            val = map(boundary)
        a.append(val)
    vals.append(a)

print(vals)
# print(min(vals))

