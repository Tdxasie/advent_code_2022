with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()


def is_safe(numbers):
    
    # diff rule
    mask = []
    for a, b in zip(numbers, numbers[1:]):
        mask.append(b-a)
    
    abs_mask = [abs(i) for i in mask]
    if len([i for i in abs_mask if i > 3]) > 1 or (len([i for i in abs_mask if i > 3]) == 1 and (abs_mask[0] != max(abs_mask) or abs_mask[-1] != max(abs_mask))):
        return False
    if len([i for i in abs_mask if i < 1]) > 1:
        return False
    
    all_neg = [i for i in mask if i<0]
    all_pos = [i for i in mask if i>0]
    
    if len(mask)-1 <= len(all_neg) <= len(mask):
        return True
    if len(mask)-1 <= len(all_pos) <= len(mask):
        return True
    
    return False
    
tot = 0
for line in lines:
    numbers = [int(i) for i in line.split(' ')]
    if is_safe(numbers):
        tot += 1
    print(numbers, is_safe(numbers), tot)
    
print(tot)