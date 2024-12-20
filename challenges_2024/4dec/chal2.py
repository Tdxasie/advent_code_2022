with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    
kernels = [
    [
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "M" , "\x00",   "M" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00",   "A" , "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "S" , "\x00",   "S" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
    ],
    [
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "S" , "\x00",   "M" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00",   "A" , "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "S" , "\x00",   "M" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
    ],
    [
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "S" , "\x00",   "S" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00",   "A" , "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "M" , "\x00",   "M" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
    ],
    [
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "M" , "\x00",   "S" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00",   "A" , "\x00", "\x00", "\x00"],
        ["\x00", "\x00",   "M" , "\x00",   "S" , "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
        ["\x00", "\x00", "\x00", "\x00", "\x00", "\x00", "\x00"],
    ],
]


nb_cols = len(lines[0])
nb_lines = len(lines)


buffer = 'b' * nb_cols

lines.insert(0, buffer)
lines.insert(0, buffer)
lines.insert(0, buffer)

lines.append(buffer)
lines.append(buffer)
lines.append(buffer)

new_lines = []
for line in lines:
    new_lines.append('bbb' + line + 'bbb')



def mul(kernel, search_zone):
    tot = 0
    for i in range(7):
        for j in range(7):
            tot += ord(kernel[i][j]) * ord(search_zone[i][j])
    return tot


magic_number = (ord('M') * ord('M'))*2 + (ord('S') * ord('S'))*2 + ord('A') * ord('A')


tot = 0
for x in range(nb_cols):
    for y in range(nb_lines):
        idxx = x + 3
        idxy = y + 3
        
        search_zone = [
            new_lines[idxx-3][idxy-3:idxy+4],
            new_lines[idxx-2][idxy-3:idxy+4],
            new_lines[idxx-1][idxy-3:idxy+4],
            new_lines[ idxx ][idxy-3:idxy+4],
            new_lines[idxx+1][idxy-3:idxy+4],
            new_lines[idxx+2][idxy-3:idxy+4],
            new_lines[idxx+3][idxy-3:idxy+4],
        ]
        
        for kernel in kernels:
            if mul(kernel, search_zone) == magic_number:
                tot += 1


print(tot)
            