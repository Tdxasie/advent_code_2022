with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()


def is_safe(numbers):
    
    # diff rule
    mask = []
    for a, b in zip(numbers, numbers[1:]):
        mask.append(b-a)
    
    abs_mask = [abs(i) for i in mask]
    if max(abs_mask) > 3:
        return False
    if min(abs_mask) < 1:
        return False
    
    all_neg = [i for i in mask if i<0]
    all_pos = [i for i in mask if i>0]
    
    if len(all_neg) == len(mask):
        return True
    if len(all_pos) == len(mask):
        return True
    
    return False
    



tot = 0
for line in lines:
    numbers = [int(i) for i in line.split(' ')]
    if is_safe(numbers):
        tot += 1
    print(numbers, is_safe(numbers), tot)
    

print(tot)