from operator import add
# start in (0,0)

instruction_times = {
    'noop': 1,
    'addx': 2,
}

interestring_values = [20, 60, 100, 140, 180, 220]


def parse_file(filename):
    with open(filename) as infile:
        lines = infile.read().splitlines()
    return lines

def print_pixel(pixel, cycle):
    print(pixel, end='')
    if cycle%40 == 0:
        print('')
        
def find_pixel(cycle, val):
    if cycle == 0:
        return 'CRT'
    
    line_pos = cycle%40
    
    if line_pos in [val-1, val, val+1]:
        return '#'
    return '.'
    
def crt(reg_vals):
    for cycle, val in enumerate(reg_vals):
        pixel = find_pixel(cycle, val)
        print_pixel(pixel, cycle)

def run_chall1(filename):
    lines = parse_file(filename)

    X = 1
    loop_count = 0
    X_values = [0]

    for line in lines:
        l = line.split(' ')
        inst = l[0]
        if len(l) > 1:
            val = int(l[1])
        time = instruction_times[inst]

        if inst == 'noop':
            loop_count += time
            X_values.append(X)
        else:
            loop_count += time
            X_values.extend([X, X := X+val])

    out = [i*X_values[i-1] for i in interestring_values]
    print(sum(out))
    
    crt(X_values)
    
if __name__ == '__main__':
    run_chall1('10dec/input.txt')
